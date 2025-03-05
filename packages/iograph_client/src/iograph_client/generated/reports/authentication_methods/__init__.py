# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .user_registration_details import UserRegistrationDetailsRequest
	from .users_registered_by_method_with_includedusertypes_includeduserroles import UsersRegisteredByMethodWithIncludedUserTypesIncludedUserRolesRequest
	from .users_registered_by_method import UsersRegisteredByMethodRequest
	from .users_registered_by_feature_with_includedusertypes_includeduserroles import UsersRegisteredByFeatureWithIncludedUserTypesIncludedUserRolesRequest
	from .users_registered_by_feature import UsersRegisteredByFeatureRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.authentication_methods_root import AuthenticationMethodsRoot


class AuthenticationMethodsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/reports/authenticationMethods", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AuthenticationMethodsRoot:
		"""
		Get authenticationMethods from reports
		Container for navigation properties for Microsoft Entra authentication methods resources.
		"""
		tags = ['reports.authenticationMethodsRoot']

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
		return await self.request_adapter.send_async(request_info, AuthenticationMethodsRoot, error_mapping)

	async def patch(
		self,
		body: AuthenticationMethodsRoot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AuthenticationMethodsRoot:
		"""
		Update the navigation property authenticationMethods in reports
		
		"""
		tags = ['reports.authenticationMethodsRoot']

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
		return await self.request_adapter.send_async(request_info, AuthenticationMethodsRoot, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property authenticationMethods for reports
		
		"""
		tags = ['reports.authenticationMethodsRoot']
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



	def with_url(self, raw_url: str) -> AuthenticationMethodsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AuthenticationMethodsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AuthenticationMethodsRequest(self.request_adapter, self.path_parameters)

	@property
	def users_registered_by_feature(self,
	) -> UsersRegisteredByFeatureRequest:
		from .users_registered_by_feature import UsersRegisteredByFeatureRequest
		return UsersRegisteredByFeatureRequest(self.request_adapter, self.path_parameters)

	def users_registered_by_feature_with_includedusertypes_includeduserroles(self,
		includedUserTypes: str,
		includedUserRoles: str,
	) -> UsersRegisteredByFeatureWithIncludedUserTypesIncludedUserRolesRequest:
		if includedUserTypes is None:
			raise TypeError("includedUserTypes cannot be null.")
		if includedUserRoles is None:
			raise TypeError("includedUserRoles cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["includedUserTypes"] =  includedUserTypes
		path_parameters["includedUserRoles"] =  includedUserRoles

		from .users_registered_by_feature_with_includedusertypes_includeduserroles import UsersRegisteredByFeatureWithIncludedUserTypesIncludedUserRolesRequest
		return UsersRegisteredByFeatureWithIncludedUserTypesIncludedUserRolesRequest(self.request_adapter, path_parameters)

	@property
	def users_registered_by_method(self,
	) -> UsersRegisteredByMethodRequest:
		from .users_registered_by_method import UsersRegisteredByMethodRequest
		return UsersRegisteredByMethodRequest(self.request_adapter, self.path_parameters)

	def users_registered_by_method_with_includedusertypes_includeduserroles(self,
		includedUserTypes: str,
		includedUserRoles: str,
	) -> UsersRegisteredByMethodWithIncludedUserTypesIncludedUserRolesRequest:
		if includedUserTypes is None:
			raise TypeError("includedUserTypes cannot be null.")
		if includedUserRoles is None:
			raise TypeError("includedUserRoles cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["includedUserTypes"] =  includedUserTypes
		path_parameters["includedUserRoles"] =  includedUserRoles

		from .users_registered_by_method_with_includedusertypes_includeduserroles import UsersRegisteredByMethodWithIncludedUserTypesIncludedUserRolesRequest
		return UsersRegisteredByMethodWithIncludedUserTypesIncludedUserRolesRequest(self.request_adapter, path_parameters)

	@property
	def user_registration_details(self,
	) -> UserRegistrationDetailsRequest:
		from .user_registration_details import UserRegistrationDetailsRequest
		return UserRegistrationDetailsRequest(self.request_adapter, self.path_parameters)

