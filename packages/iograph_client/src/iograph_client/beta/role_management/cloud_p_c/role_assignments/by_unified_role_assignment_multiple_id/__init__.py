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
	from .role_definition import RoleDefinitionRequest
	from .principals import PrincipalsRequest
	from .directory_scopes import DirectoryScopesRequest
	from .app_scopes import AppScopesRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.unified_role_assignment_multiple import UnifiedRoleAssignmentMultiple


class ByUnifiedRoleAssignmentMultipleIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/roleManagement/cloudPC/roleAssignments/{unifiedRoleAssignmentMultiple%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UnifiedRoleAssignmentMultiple:
		"""
		Get unifiedRoleAssignmentMultiple
		Get the properties and relationships of a unifiedRoleAssignmentMultiple object of an RBAC provider.  The following RBAC providers are currently supported:
- Cloud PC 
- device management (Intune) For other Microsoft 365 applications (like Microsoft Entra ID), use unifiedRoleAssignment.
		Find more info here: https://learn.microsoft.com/graph/api/unifiedroleassignmentmultiple-get?view=graph-rest-beta
		"""
		tags = ['roleManagement.rbacApplicationMultiple']

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
		return await self.request_adapter.send_async(request_info, UnifiedRoleAssignmentMultiple, error_mapping)

	async def patch(
		self,
		body: UnifiedRoleAssignmentMultiple,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UnifiedRoleAssignmentMultiple:
		"""
		Update unifiedRoleAssignmentMultiple
		Update an existing unifiedRoleAssignmentMultiple object of an RBAC provider.  The following RBAC providers are currently supported:
- Cloud PC 
- device management (Intune) In contrast, unifiedRoleAssignment does not support update.
		Find more info here: https://learn.microsoft.com/graph/api/unifiedroleassignmentmultiple-update?view=graph-rest-beta
		"""
		tags = ['roleManagement.rbacApplicationMultiple']

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
		return await self.request_adapter.send_async(request_info, UnifiedRoleAssignmentMultiple, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete unifiedRoleAssignmentMultiple
		Delete a unifiedRoleAssignmentMultiple object of an RBAC provider.  This is applicable for a RBAC application that supports multiple principals and scopes. The following RBAC providers are currently supported:
- Cloud PC 
- device management (Intune)
		Find more info here: https://learn.microsoft.com/graph/api/unifiedroleassignmentmultiple-delete?view=graph-rest-beta
		"""
		tags = ['roleManagement.rbacApplicationMultiple']
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



	def with_url(self, raw_url: str) -> ByUnifiedRoleAssignmentMultipleIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUnifiedRoleAssignmentMultipleIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUnifiedRoleAssignmentMultipleIdRequest(self.request_adapter, self.path_parameters)

	def app_scopes(self,
		unifiedRoleAssignmentMultiple_id: str,
	) -> AppScopesRequest:
		if unifiedRoleAssignmentMultiple_id is None:
			raise TypeError("unifiedRoleAssignmentMultiple_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["unifiedRoleAssignmentMultiple%2Did"] =  unifiedRoleAssignmentMultiple_id

		from .app_scopes import AppScopesRequest
		return AppScopesRequest(self.request_adapter, path_parameters)

	def directory_scopes(self,
		unifiedRoleAssignmentMultiple_id: str,
	) -> DirectoryScopesRequest:
		if unifiedRoleAssignmentMultiple_id is None:
			raise TypeError("unifiedRoleAssignmentMultiple_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["unifiedRoleAssignmentMultiple%2Did"] =  unifiedRoleAssignmentMultiple_id

		from .directory_scopes import DirectoryScopesRequest
		return DirectoryScopesRequest(self.request_adapter, path_parameters)

	def principals(self,
		unifiedRoleAssignmentMultiple_id: str,
	) -> PrincipalsRequest:
		if unifiedRoleAssignmentMultiple_id is None:
			raise TypeError("unifiedRoleAssignmentMultiple_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["unifiedRoleAssignmentMultiple%2Did"] =  unifiedRoleAssignmentMultiple_id

		from .principals import PrincipalsRequest
		return PrincipalsRequest(self.request_adapter, path_parameters)

	def role_definition(self,
		unifiedRoleAssignmentMultiple_id: str,
	) -> RoleDefinitionRequest:
		if unifiedRoleAssignmentMultiple_id is None:
			raise TypeError("unifiedRoleAssignmentMultiple_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["unifiedRoleAssignmentMultiple%2Did"] =  unifiedRoleAssignmentMultiple_id

		from .role_definition import RoleDefinitionRequest
		return RoleDefinitionRequest(self.request_adapter, path_parameters)

