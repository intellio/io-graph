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
	from .policy import PolicyRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByUnifiedRoleManagementPolicyAssignmentIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/policies/roleManagementPolicyAssignments/{unifiedRoleManagementPolicyAssignment%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UnifiedRoleManagementPolicyAssignment:
		"""
		Get unifiedRoleManagementPolicyAssignment
		Get the details of a policy assignment in PIM that's assigned to Microsoft Entra roles or group membership or ownership.
		Find more info here: https://learn.microsoft.com/graph/api/unifiedrolemanagementpolicyassignment-get?view=graph-rest-1.0
		"""
		tags = ['policies.unifiedRoleManagementPolicyAssignment']

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
		return await self.request_adapter.send_async(request_info, UnifiedRoleManagementPolicyAssignment, error_mapping)

	async def patch(
		self,
		body: UnifiedRoleManagementPolicyAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UnifiedRoleManagementPolicyAssignment:
		"""
		Update the navigation property roleManagementPolicyAssignments in policies
		
		"""
		tags = ['policies.unifiedRoleManagementPolicyAssignment']

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
		return await self.request_adapter.send_async(request_info, UnifiedRoleManagementPolicyAssignment, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property roleManagementPolicyAssignments for policies
		
		"""
		tags = ['policies.unifiedRoleManagementPolicyAssignment']
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



	def with_url(self, raw_url: str) -> ByUnifiedRoleManagementPolicyAssignmentIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUnifiedRoleManagementPolicyAssignmentIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUnifiedRoleManagementPolicyAssignmentIdRequest(self.request_adapter, self.path_parameters)

	def policy(self,
		unifiedRoleManagementPolicyAssignment_id: str,
	) -> PolicyRequest:
		if unifiedRoleManagementPolicyAssignment_id is None:
			raise TypeError("unifiedRoleManagementPolicyAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["unifiedRoleManagementPolicyAssignment%2Did"] =  unifiedRoleManagementPolicyAssignment_id

		from .policy import PolicyRequest
		return PolicyRequest(self.request_adapter, path_parameters)

