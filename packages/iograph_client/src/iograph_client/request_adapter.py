from typing import Any, Optional, Union, TypeVar
import re
from urllib import parse
import httpx
from uuid import UUID
from datetime import timedelta, date, time, datetime
from string import Template
from pydantic import BaseModel
from kiota_abstractions.authentication import AuthenticationProvider
from kiota_abstractions.request_information import RequestInformation
from .exceptions import (
    RequestError,
    ResponseError,
    APIError,
)

ModelType = TypeVar("ModelType", bound=BaseModel)
ResponseType = TypeVar("ResponseType")
PrimitiveType = TypeVar(
    "PrimitiveType", bool, str, int, float, UUID, datetime, timedelta, date, time, bytes
)
REQUEST_IS_NULL = RequestError("Request info cannot be null")


class HttpxRequestAdapter:
    CLAIMS_KEY = "claims"
    BEARER_AUTHENTICATION_SCHEME = "Bearer"
    RESPONSE_AUTH_HEADER = "WWW-Authenticate"

    # pylint: disable=too-many-positional-arguments
    def __init__(
        self,
        authentication_provider: AuthenticationProvider,
        http_client: Optional[httpx.AsyncClient] = None,
        base_url: Optional[str] = None,
        api_version: Optional[str] = None,
    ) -> None:

        if not authentication_provider:
            raise TypeError("Authentication provider cannot be null")
        self._authentication_provider = authentication_provider

        if not http_client:
            raise TypeError("HTTP client cannot be null")
        self._http_client: httpx.AsyncClient = http_client

        if not base_url:
            base_url = (
                str(http_client.base_url) if http_client.base_url is not None else ""
            )
        else:
            base_url = Template("$base/$ver").safe_substitute(base=base_url, ver=api_version)
        self._base_url: str = base_url

    @property
    def base_url(self) -> str:
        """Gets the base url for every request

        Returns:
            str: The base url
        """
        return (
            self._base_url or str(self._http_client.base_url)
            if self._http_client.base_url is not None
            else ""
        )

    @base_url.setter
    def base_url(self, value: str) -> None:
        """Sets the base url for every request

        Args:
            value (str): The new base url
        """
        if value:
            self._base_url = value

    async def send_async(
        self,
        request_info: RequestInformation,
        return_model: ModelType,
        error_map: Optional[dict[str, type[BaseModel]]],
    ) -> Optional[ModelType]:
        """Excutes the HTTP request specified by the given RequestInformation and returns the
        deserialized response model.
        Args:
            request_info (RequestInformation): the request info to execute.
            parsable_factory (ParsableFactory): the class of the response model
            to deserialize the response into.
            error_map (dict[str, type[ParsableFactory]]): the error dict to use in
            case of a failed request.

        Returns:
            ModelType: the deserialized response model.
        """
        try:
            if not request_info:
                raise REQUEST_IS_NULL

            response = await self.get_http_response_message(request_info)

            await self.throw_failed_responses(response,error_map)
            
            if self._should_return_none(response):
                return None
            
            value = return_model.model_validate_json(response.text)


            return value  # type: ignore
        except Exception as exc:
            raise exc
        finally:
            pass

    async def send_collection_async(
        self,
        request_info: RequestInformation,
        return_model: ModelType,
        error_map: Optional[dict[str, type[BaseModel]]],
    ) -> Optional[list[ModelType]]:
        """Excutes the HTTP request specified by the given RequestInformation and returns the
        deserialized response model collection.
        Args:
            request_info (RequestInformation): the request info to execute.
            parsable_factory (ParsableFactory): the class of the response model
            to deserialize the response into.
            error_map (dict[str, type[ParsableFactory]]): the error dict to use in
            case of a failed request.

        Returns:
            ModelType: the deserialized response model collection.
        """
        try:
            if not request_info:
                raise REQUEST_IS_NULL
            
            response = await self.get_http_response_message(request_info)

            await self.throw_failed_responses(response, error_map,)

            if self._should_return_none(response):
                return None


            json = response.json()
            if isinstance(json, list):
                result: Optional[list[ModelType]] =[return_model.model_validate_json(str(item)) for item in json]
            else:
                # raise error
                raise ResponseError("Response is not a collection")
            
            return result

        except Exception as exc:
            raise exc
        finally:
            pass

    async def send_primitive_async(
        self,
        request_info: RequestInformation,
        response_type: str,
        error_map: Optional[dict[str, type[BaseModel]]],
    ) -> Optional[ResponseType]:
        """Excutes the HTTP request specified by the given RequestInformation and returns the
        deserialized primitive response model.
        Args:
            request_info (RequestInformation): the request info to execute.
            response_type (str): the class name of the response model to deserialize the
            response into.
            error_map (dict[str, type[ParsableFactory]]): the error dict to use in case
            of a failed request.

        Returns:
            Optional[ResponseType]: the deserialized primitive response model.
        """
        try:
            if not request_info:
                raise REQUEST_IS_NULL

            response = await self.get_http_response_message(request_info)

            await self.throw_failed_responses(response, error_map,)

            if self._should_return_none(response):
                return None

            if response_type == "bytes":
                return response.content  # type: ignore

            value: Optional[Union[str, int, float, bool, datetime, bytes]] = None
            if response_type == "str":
                value = response.text
            if response_type == "int":
                value = int(response.text)
            if response_type == "float":
                value = float(response.text)
            if response_type == "bool":
                value = bool(response.text)
            if response_type == "datetime":
                value = datetime.fromisoformat(response.text)

            if value is not None:
                return value  # type: ignore
            else:
                raise TypeError(f"Error handling the response, unexpected type {response_type!r}")
        except Exception as exc:
            raise exc

        finally:
            pass

    async def send_no_response_content_async(
        self,
        request_info: RequestInformation,
        error_map: Optional[dict[str, type[BaseModel]]],
    ) -> None:
        """Excutes the HTTP request specified by the given RequestInformation and returns the
        deserialized primitive response model.
        Args:
            request_info (RequestInformation):the request info to execute.
            error_map (dict[str, type[ParsableFactory]]): the error dict to use in case
            of a failed request.
        """
        try:
            if not request_info:
                raise REQUEST_IS_NULL

            response = await self.get_http_response_message(request_info)
            
            await self.throw_failed_responses(response, error_map)
        finally:
            pass

    def set_base_url_for_request_information(
        self, request_info: RequestInformation
    ) -> None:
        request_info.path_parameters["baseurl"] = self.base_url

    def get_request_from_request_information(
        self,
        request_info: RequestInformation,
    ) -> httpx.Request:

        url = parse.urlparse(request_info.url)
        method = request_info.http_method
        if not method:
            raise RequestError("HTTP method must be provided")

        request = self._http_client.build_request(
            method=method.value,
            url=request_info.url,
            headers=request_info.request_headers,
            content=request_info.content,
            params=request_info.query_parameters,
        )

        return request

    async def retry_cae_response_if_required(
        self, resp: httpx.Response, request_info: RequestInformation, claims: str
    ) -> httpx.Response:
        if (
            resp.status_code == 401
            and not claims  # previous claims exist. Means request has already been retried
            and resp.headers.get(self.RESPONSE_AUTH_HEADER)
        ):
            auth_header_value = resp.headers.get(self.RESPONSE_AUTH_HEADER)
            if auth_header_value.casefold().startswith(
                self.BEARER_AUTHENTICATION_SCHEME.casefold()
            ):
                claims_match = re.search('claims="([^"]+)"', auth_header_value)
                if not claims_match:
                    raise ValueError("Unable to parse claims from response")
                response_claims = claims_match.group(1)
                return await self.get_http_response_message(
                    request_info, response_claims
                )
            return resp
        return resp

    async def get_http_response_message(
        self,
        request_info: RequestInformation,
        claims: str = "",
    ) -> httpx.Response:

        self.set_base_url_for_request_information(request_info)

        additional_authentication_context = {}
        if claims:
            additional_authentication_context[self.CLAIMS_KEY] = claims

        await self._authentication_provider.authenticate_request(
            request_info, additional_authentication_context
        )

        request = self.get_request_from_request_information(request_info)
        resp = await self._http_client.send(request)
        if not resp:
            raise ResponseError("Unable to get response from request")
        
        if http_version := resp.http_version:
            pass
            # print("http_version: ", http_version)

        if content_length := resp.headers.get("Content-Length", None):
            pass
            # print("content_length: ", content_length)

        if content_type := resp.headers.get("Content-Type", None):
            pass
            # print("content_type: ", content_type)

        return await self.retry_cae_response_if_required(resp, request_info, claims)

    def _is_redirect_missing_location(
        self,
        response: httpx.Response,
    ) -> bool:
        if response.is_redirect:
            if response.has_redirect_location:
                return False
            # Raise a more specific error if the server returned a redirect status code
            # without a location header
            exc = APIError(
                f"The server returned a redirect status code {response.status_code}"
                " without a location header",
                response.status_code,
                response.headers,  # type: ignore
            )
            raise exc
        return True

    def _error_class_not_in_error_mapping(
        self, error_map: dict[str, type[BaseModel]], status_code: int
    ) -> bool:
        """Helper function to check if the error class corresponding to a response status code
        is not in the error mapping.

        Args:
            error_map (dict[str, type[ParsableFactory]]): The error mapping.
            status_code (int): The response status code.

        Returns:
            bool: True if the error class is not in the error mapping, False otherwise.
        """

        return (
            (400 <= status_code < 500 and "4XX" not in error_map)
            or (500 <= status_code < 600 and "5XX" not in error_map)
        ) and ("XXX" not in error_map)

    async def _get_error_from_response(
        self,
        response: httpx.Response,
        error_map: dict[str, type[BaseModel]],
        response_status_code_str: str,
        response_status_code: int,
    ) -> object:
        error_class = None
        if response_status_code_str in error_map:  # Error Code 400 - <= 599
            error_class = error_map[response_status_code_str]
        elif 400 <= response_status_code < 500 and "4XX" in error_map:  # Error code 4XX
            error_class = error_map["4XX"]
        elif 500 <= response_status_code < 600 and "5XX" in error_map:  # Error code 5XX
            error_class = error_map["5XX"]
        elif "XXX" in error_map:  # Blanket case
            error_class = error_map["XXX"]

        error = None
        if error_class:
            error = error_class.model_validate_json(response.text)
            error = APIError(
                error.model_dump_json(),
                response_status_code,
            )
        return error

    async def throw_failed_responses(
        self,
        response: httpx.Response,
        error_map: Optional[dict[str, BaseModel]],
    ) -> None:
        if response.is_success or response.status_code == 304:
            return
        if self._is_redirect_missing_location(response) is False:
            return
        try:

            response_status_code = response.status_code
            response_status_code_str = str(response_status_code)
            response_headers = response.headers

            if not error_map:
                exc = APIError(
                    "The server returned an unexpected status code and no error class is registered"
                    f" for this code {response_status_code}",
                    response_status_code,
                    response_headers,  # type: ignore
                )
                raise exc

            if (
                response_status_code_str not in error_map
                and self._error_class_not_in_error_mapping(
                    error_map, response_status_code
                )
            ):
                exc = APIError(
                    "The server returned an unexpected status code and no error class is registered"
                    f" for this code {response_status_code}",
                    response_status_code,
                    response_headers,  # type: ignore
                )
                raise exc

            error = await self._get_error_from_response(
                response,
                error_map,
                response_status_code_str,
                response_status_code,
            )
            if isinstance(error, APIError):
                error.response_headers = response_headers  # type: ignore
                error.response_status_code = response_status_code
                exc = error
            else:
                exc = APIError(
                    (
                        "The server returned an unexpected status code and the error registered"
                        f" for this code failed to deserialize: {type(error)}"
                    ),
                    response_status_code,
                    response_headers,  # type: ignore
                )
            raise exc
        finally:
            pass

    def _should_return_none(self, response: httpx.Response) -> bool:
        """Helper function to check if the response should return None.

        Conditions:
            - The response status code is 204 or 304
            - the response content is empty.
            - The response status code is 301 or 302 and the location header is not present.

        Returns:
            bool: True if the response should return None, False otherwise.
        """
        return (
            response.status_code == 204
            or response.status_code == 304
            or not bool(response.content)
            or (
                not response.headers.get("location")
                and response.status_code in [301, 302]
            )
        )

    async def convert_to_native_async(
        self, request_info: RequestInformation
    ) -> httpx.Request:
        try:
            if request_info is None:
                exc = ValueError("request information must be provided")
                raise exc

            await self._authentication_provider.authenticate_request(request_info)

            request = self.get_request_from_request_information(
                request_info,
            )
            return request
        finally:
            pass

    async def send_collection_of_primitive_async(
        self,
        request_info: RequestInformation,
        response_type: type[PrimitiveType],
        error_map: Optional[dict[str, type[BaseModel]]],
    ) -> Optional[list[PrimitiveType]]:
        """Excutes the HTTP request specified by the given RequestInformation and returns the
        deserialized response model collection.
        Args:
            request_info (RequestInformation): the request info to execute.
            response_type (PrimitiveType): the class of the response model
            to deserialize the response into.
            error_map (dict[str, type[ParsableFactory]]): the error dict to use in
            case of a failed request.

        Returns:
            Optional[list[PrimitiveType]]: The deserialized primitive type collection.
        """
        raise NotImplementedError("Method not implemented")
        try:
            if not request_info:
                raise REQUEST_IS_NULL

            response = await self.get_http_response_message(request_info)

            await self.throw_failed_responses(response, error_map,)
            if self._should_return_none(response):
                return None


            if response.content:
                
                return values  # type: ignore
            else:
                return None
        finally:
            pass