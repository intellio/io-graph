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
	from .windows_hello_for_business_methods import WindowsHelloForBusinessMethodsRequest
	from .temporary_access_pass_methods import TemporaryAccessPassMethodsRequest
	from .software_oath_methods import SoftwareOathMethodsRequest
	from .phone_methods import PhoneMethodsRequest
	from .password_methods import PasswordMethodsRequest
	from .operations import OperationsRequest
	from .microsoft_authenticator_methods import MicrosoftAuthenticatorMethodsRequest
	from .methods import MethodsRequest
	from .fido2_methods import Fido2MethodsRequest
	from .email_methods import EmailMethodsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.authentication import Authentication
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class AuthenticationRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/authentication", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Authentication:
		"""
		Get authentication from users
		The authentication methods that are supported for the user.
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
		return await self.request_adapter.send_async(request_info, Authentication, error_mapping)

	async def patch(
		self,
		body: Authentication,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Authentication:
		"""
		Update the navigation property authentication in users
		
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
		return await self.request_adapter.send_async(request_info, Authentication, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property authentication for users
		
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



	def with_url(self, raw_url: str) -> AuthenticationRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AuthenticationRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AuthenticationRequest(self.request_adapter, self.path_parameters)

	def email_methods(self,
		user_id: str,
	) -> EmailMethodsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .email_methods import EmailMethodsRequest
		return EmailMethodsRequest(self.request_adapter, path_parameters)

	def fido2_methods(self,
		user_id: str,
	) -> Fido2MethodsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .fido2_methods import Fido2MethodsRequest
		return Fido2MethodsRequest(self.request_adapter, path_parameters)

	def methods(self,
		user_id: str,
	) -> MethodsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .methods import MethodsRequest
		return MethodsRequest(self.request_adapter, path_parameters)

	def microsoft_authenticator_methods(self,
		user_id: str,
	) -> MicrosoftAuthenticatorMethodsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .microsoft_authenticator_methods import MicrosoftAuthenticatorMethodsRequest
		return MicrosoftAuthenticatorMethodsRequest(self.request_adapter, path_parameters)

	def operations(self,
		user_id: str,
	) -> OperationsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, path_parameters)

	def password_methods(self,
		user_id: str,
	) -> PasswordMethodsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .password_methods import PasswordMethodsRequest
		return PasswordMethodsRequest(self.request_adapter, path_parameters)

	def phone_methods(self,
		user_id: str,
	) -> PhoneMethodsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .phone_methods import PhoneMethodsRequest
		return PhoneMethodsRequest(self.request_adapter, path_parameters)

	def software_oath_methods(self,
		user_id: str,
	) -> SoftwareOathMethodsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .software_oath_methods import SoftwareOathMethodsRequest
		return SoftwareOathMethodsRequest(self.request_adapter, path_parameters)

	def temporary_access_pass_methods(self,
		user_id: str,
	) -> TemporaryAccessPassMethodsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .temporary_access_pass_methods import TemporaryAccessPassMethodsRequest
		return TemporaryAccessPassMethodsRequest(self.request_adapter, path_parameters)

	def windows_hello_for_business_methods(self,
		user_id: str,
	) -> WindowsHelloForBusinessMethodsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .windows_hello_for_business_methods import WindowsHelloForBusinessMethodsRequest
		return WindowsHelloForBusinessMethodsRequest(self.request_adapter, path_parameters)

