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
	from .reset_password import ResetPasswordRequest
	from .enable_sms_sign_in import EnableSmsSignInRequest
	from .disable_sms_sign_in import DisableSmsSignInRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.authentication_method import AuthenticationMethod


class ByAuthenticationMethodIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/authentication/methods/{authenticationMethod%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AuthenticationMethod:
		"""
		Get authenticationMethod
		Retrieve the properties and relationships of an authenticationMethod object.
		Find more info here: https://learn.microsoft.com/graph/api/authenticationmethod-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, AuthenticationMethod, error_mapping)

	async def patch(
		self,
		body: AuthenticationMethod,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AuthenticationMethod:
		"""
		Update the navigation property methods in me
		
		"""
		tags = ['me.authentication']

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
		return await self.request_adapter.send_async(request_info, AuthenticationMethod, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ByAuthenticationMethodIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAuthenticationMethodIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAuthenticationMethodIdRequest(self.request_adapter, self.path_parameters)

	def disable_sms_sign_in(self,
		authenticationMethod_id: str,
	) -> DisableSmsSignInRequest:
		if authenticationMethod_id is None:
			raise TypeError("authenticationMethod_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["authenticationMethod%2Did"] =  authenticationMethod_id

		from .disable_sms_sign_in import DisableSmsSignInRequest
		return DisableSmsSignInRequest(self.request_adapter, path_parameters)

	def enable_sms_sign_in(self,
		authenticationMethod_id: str,
	) -> EnableSmsSignInRequest:
		if authenticationMethod_id is None:
			raise TypeError("authenticationMethod_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["authenticationMethod%2Did"] =  authenticationMethod_id

		from .enable_sms_sign_in import EnableSmsSignInRequest
		return EnableSmsSignInRequest(self.request_adapter, path_parameters)

	def reset_password(self,
		authenticationMethod_id: str,
	) -> ResetPasswordRequest:
		if authenticationMethod_id is None:
			raise TypeError("authenticationMethod_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["authenticationMethod%2Did"] =  authenticationMethod_id

		from .reset_password import ResetPasswordRequest
		return ResetPasswordRequest(self.request_adapter, path_parameters)

