# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .access_package_resource_scope import AccessPackageResourceScopeRequest
	from .access_package_resource_role import AccessPackageResourceRoleRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.access_package_resource_role_scope import AccessPackageResourceRoleScope


class ByAccessPackageResourceRoleScopeIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackages/{accessPackage%2Did}/accessPackageResourceRoleScopes/{accessPackageResourceRoleScope%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessPackageResourceRoleScope:
		"""
		Get accessPackageResourceRoleScopes from identityGovernance
		
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, AccessPackageResourceRoleScope, error_mapping)

	async def patch(
		self,
		body: AccessPackageResourceRoleScope,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessPackageResourceRoleScope:
		"""
		Update the navigation property accessPackageResourceRoleScopes in identityGovernance
		
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, AccessPackageResourceRoleScope, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property accessPackageResourceRoleScopes for identityGovernance
		
		"""
		tags = ['identityGovernance.entitlementManagement']
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



	def with_url(self, raw_url: str) -> ByAccessPackageResourceRoleScopeIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAccessPackageResourceRoleScopeIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAccessPackageResourceRoleScopeIdRequest(self.request_adapter, self.path_parameters)

	def access_package_resource_role(self,
		accessPackage_id: str,
		accessPackageResourceRoleScope_id: str,
	) -> AccessPackageResourceRoleRequest:
		if accessPackage_id is None:
			raise TypeError("accessPackage_id cannot be null.")
		if accessPackageResourceRoleScope_id is None:
			raise TypeError("accessPackageResourceRoleScope_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackage%2Did"] =  accessPackage_id
		path_parameters["accessPackageResourceRoleScope%2Did"] =  accessPackageResourceRoleScope_id

		from .access_package_resource_role import AccessPackageResourceRoleRequest
		return AccessPackageResourceRoleRequest(self.request_adapter, path_parameters)

	def access_package_resource_scope(self,
		accessPackage_id: str,
		accessPackageResourceRoleScope_id: str,
	) -> AccessPackageResourceScopeRequest:
		if accessPackage_id is None:
			raise TypeError("accessPackage_id cannot be null.")
		if accessPackageResourceRoleScope_id is None:
			raise TypeError("accessPackageResourceRoleScope_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackage%2Did"] =  accessPackage_id
		path_parameters["accessPackageResourceRoleScope%2Did"] =  accessPackageResourceRoleScope_id

		from .access_package_resource_scope import AccessPackageResourceScopeRequest
		return AccessPackageResourceScopeRequest(self.request_adapter, path_parameters)

