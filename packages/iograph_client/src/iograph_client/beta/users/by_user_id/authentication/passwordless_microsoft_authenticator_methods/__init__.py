# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_passwordless_microsoft_authenticator_authentication_method_id import ByPasswordlessMicrosoftAuthenticatorAuthenticationMethodIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.passwordless_microsoft_authenticator_authentication_method_collection_response import PasswordlessMicrosoftAuthenticatorAuthenticationMethodCollectionResponse


class PasswordlessMicrosoftAuthenticatorMethodsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/authentication/passwordlessMicrosoftAuthenticatorMethods", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PasswordlessMicrosoftAuthenticatorAuthenticationMethodCollectionResponse:
		"""
		Get passwordlessMicrosoftAuthenticatorMethods from users
		Represents the Microsoft Authenticator Passwordless Phone Sign-in methods registered to a user for authentication.
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
		return await self.request_adapter.send_async(request_info, PasswordlessMicrosoftAuthenticatorAuthenticationMethodCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> PasswordlessMicrosoftAuthenticatorMethodsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PasswordlessMicrosoftAuthenticatorMethodsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PasswordlessMicrosoftAuthenticatorMethodsRequest(self.request_adapter, self.path_parameters)

	def by_passwordless_microsoft_authenticator_authentication_method_id(self,
		user_id: str,
		passwordlessMicrosoftAuthenticatorAuthenticationMethod_id: str,
	) -> ByPasswordlessMicrosoftAuthenticatorAuthenticationMethodIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if passwordlessMicrosoftAuthenticatorAuthenticationMethod_id is None:
			raise TypeError("passwordlessMicrosoftAuthenticatorAuthenticationMethod_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["passwordlessMicrosoftAuthenticatorAuthenticationMethod%2Did"] =  passwordlessMicrosoftAuthenticatorAuthenticationMethod_id

		from .by_passwordless_microsoft_authenticator_authentication_method_id import ByPasswordlessMicrosoftAuthenticatorAuthenticationMethodIdRequest
		return ByPasswordlessMicrosoftAuthenticatorAuthenticationMethodIdRequest(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

