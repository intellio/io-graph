# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_microsoft_authenticator_authentication_method_id import ByMicrosoftAuthenticatorAuthenticationMethodIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.microsoft_authenticator_authentication_method_collection_response import MicrosoftAuthenticatorAuthenticationMethodCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class MicrosoftAuthenticatorMethodsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/authentication/microsoftAuthenticatorMethods", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MicrosoftAuthenticatorAuthenticationMethodCollectionResponse:
		"""
		Get microsoftAuthenticatorMethods from me
		The details of the Microsoft Authenticator app registered to a user for authentication.
		"""
		tags = ['me.authentication']

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
		return await self.request_adapter.send_async(request_info, MicrosoftAuthenticatorAuthenticationMethodCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> MicrosoftAuthenticatorMethodsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MicrosoftAuthenticatorMethodsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MicrosoftAuthenticatorMethodsRequest(self.request_adapter, self.path_parameters)

	def by_microsoft_authenticator_authentication_method_id(self,
		microsoftAuthenticatorAuthenticationMethod_id: str,
	) -> ByMicrosoftAuthenticatorAuthenticationMethodIdRequest:
		if microsoftAuthenticatorAuthenticationMethod_id is None:
			raise TypeError("microsoftAuthenticatorAuthenticationMethod_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["microsoftAuthenticatorAuthenticationMethod%2Did"] =  microsoftAuthenticatorAuthenticationMethod_id

		from .by_microsoft_authenticator_authentication_method_id import ByMicrosoftAuthenticatorAuthenticationMethodIdRequest
		return ByMicrosoftAuthenticatorAuthenticationMethodIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

