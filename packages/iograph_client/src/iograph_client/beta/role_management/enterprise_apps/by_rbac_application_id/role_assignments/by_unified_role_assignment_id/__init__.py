# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .role_definition import RoleDefinitionRequest
	from .principal import PrincipalRequest
	from .directory_scope import DirectoryScopeRequest
	from .app_scope import AppScopeRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.unified_role_assignment import UnifiedRoleAssignment
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByUnifiedRoleAssignmentIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/roleManagement/enterpriseApps/{rbacApplication%2Did}/roleAssignments/{unifiedRoleAssignment%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UnifiedRoleAssignment:
		"""
		Get roleAssignments from roleManagement
		
		"""
		tags = ['roleManagement.rbacApplication']

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
		return await self.request_adapter.send_async(request_info, UnifiedRoleAssignment, error_mapping)

	async def patch(
		self,
		body: UnifiedRoleAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UnifiedRoleAssignment:
		"""
		Update the navigation property roleAssignments in roleManagement
		
		"""
		tags = ['roleManagement.rbacApplication']

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
		return await self.request_adapter.send_async(request_info, UnifiedRoleAssignment, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property roleAssignments for roleManagement
		
		"""
		tags = ['roleManagement.rbacApplication']
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



	def with_url(self, raw_url: str) -> ByUnifiedRoleAssignmentIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUnifiedRoleAssignmentIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUnifiedRoleAssignmentIdRequest(self.request_adapter, self.path_parameters)

	def app_scope(self,
		rbacApplication_id: str,
		unifiedRoleAssignment_id: str,
	) -> AppScopeRequest:
		if rbacApplication_id is None:
			raise TypeError("rbacApplication_id cannot be null.")
		if unifiedRoleAssignment_id is None:
			raise TypeError("unifiedRoleAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["rbacApplication%2Did"] =  rbacApplication_id
		path_parameters["unifiedRoleAssignment%2Did"] =  unifiedRoleAssignment_id

		from .app_scope import AppScopeRequest
		return AppScopeRequest(self.request_adapter, path_parameters)

	def directory_scope(self,
		rbacApplication_id: str,
		unifiedRoleAssignment_id: str,
	) -> DirectoryScopeRequest:
		if rbacApplication_id is None:
			raise TypeError("rbacApplication_id cannot be null.")
		if unifiedRoleAssignment_id is None:
			raise TypeError("unifiedRoleAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["rbacApplication%2Did"] =  rbacApplication_id
		path_parameters["unifiedRoleAssignment%2Did"] =  unifiedRoleAssignment_id

		from .directory_scope import DirectoryScopeRequest
		return DirectoryScopeRequest(self.request_adapter, path_parameters)

	def principal(self,
		rbacApplication_id: str,
		unifiedRoleAssignment_id: str,
	) -> PrincipalRequest:
		if rbacApplication_id is None:
			raise TypeError("rbacApplication_id cannot be null.")
		if unifiedRoleAssignment_id is None:
			raise TypeError("unifiedRoleAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["rbacApplication%2Did"] =  rbacApplication_id
		path_parameters["unifiedRoleAssignment%2Did"] =  unifiedRoleAssignment_id

		from .principal import PrincipalRequest
		return PrincipalRequest(self.request_adapter, path_parameters)

	def role_definition(self,
		rbacApplication_id: str,
		unifiedRoleAssignment_id: str,
	) -> RoleDefinitionRequest:
		if rbacApplication_id is None:
			raise TypeError("rbacApplication_id cannot be null.")
		if unifiedRoleAssignment_id is None:
			raise TypeError("unifiedRoleAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["rbacApplication%2Did"] =  rbacApplication_id
		path_parameters["unifiedRoleAssignment%2Did"] =  unifiedRoleAssignment_id

		from .role_definition import RoleDefinitionRequest
		return RoleDefinitionRequest(self.request_adapter, path_parameters)

