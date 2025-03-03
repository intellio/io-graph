# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.email_authentication_method import EmailAuthenticationMethod
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByEmailAuthenticationMethodIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/authentication/emailMethods/{emailAuthenticationMethod%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EmailAuthenticationMethod:
		"""
		Get emailMethods from users
		The email address registered to a user for authentication.
		"""
		tags = ['users.authentication']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.GET,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_async(request_info, EmailAuthenticationMethod, error_mapping)

	async def patch(
		self,
		body: EmailAuthenticationMethod,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EmailAuthenticationMethod:
		"""
		Update emailAuthenticationMethod
		Update a user's email address represented by an emailAuthenticationMethod object. Self-service operations aren't supported.
		Find more info here: https://learn.microsoft.com/graph/api/emailauthenticationmethod-update?view=graph-rest-1.0
		"""
		tags = ['users.authentication']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, EmailAuthenticationMethod, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete emailAuthenticationMethod
		Deletes a user's emailAuthenticationMethod object.
		Find more info here: https://learn.microsoft.com/graph/api/emailauthenticationmethod-delete?view=graph-rest-1.0
		"""
		tags = ['users.authentication']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> ByEmailAuthenticationMethodIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByEmailAuthenticationMethodIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByEmailAuthenticationMethodIdRequest(self.request_adapter, self.path_parameters)

