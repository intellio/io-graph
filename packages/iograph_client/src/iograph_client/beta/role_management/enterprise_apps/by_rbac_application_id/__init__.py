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
	from .transitive_role_assignments import TransitiveRoleAssignmentsRequest
	from .role_eligibility_schedules import RoleEligibilitySchedulesRequest
	from .role_eligibility_schedule_requests import RoleEligibilityScheduleRequestsRequest
	from .role_eligibility_schedule_instances import RoleEligibilityScheduleInstancesRequest
	from .role_definitions import RoleDefinitionsRequest
	from .role_assignment_schedules import RoleAssignmentSchedulesRequest
	from .role_assignment_schedule_requests import RoleAssignmentScheduleRequestsRequest
	from .role_assignment_schedule_instances import RoleAssignmentScheduleInstancesRequest
	from .role_assignments import RoleAssignmentsRequest
	from .role_assignment_approvals import RoleAssignmentApprovalsRequest
	from .resource_namespaces import ResourceNamespacesRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.rbac_application import RbacApplication


class ByRbacApplicationIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/roleManagement/enterpriseApps/{rbacApplication%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> RbacApplication:
		"""
		Get enterpriseApps from roleManagement
		
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
		return await self.request_adapter.send_async(request_info, RbacApplication, error_mapping)

	async def patch(
		self,
		body: RbacApplication,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> RbacApplication:
		"""
		Update the navigation property enterpriseApps in roleManagement
		
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
		return await self.request_adapter.send_async(request_info, RbacApplication, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property enterpriseApps for roleManagement
		
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



	def with_url(self, raw_url: str) -> ByRbacApplicationIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByRbacApplicationIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByRbacApplicationIdRequest(self.request_adapter, self.path_parameters)

	def resource_namespaces(self,
		rbacApplication_id: str,
	) -> ResourceNamespacesRequest:
		if rbacApplication_id is None:
			raise TypeError("rbacApplication_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["rbacApplication%2Did"] =  rbacApplication_id

		from .resource_namespaces import ResourceNamespacesRequest
		return ResourceNamespacesRequest(self.request_adapter, path_parameters)

	def role_assignment_approvals(self,
		rbacApplication_id: str,
	) -> RoleAssignmentApprovalsRequest:
		if rbacApplication_id is None:
			raise TypeError("rbacApplication_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["rbacApplication%2Did"] =  rbacApplication_id

		from .role_assignment_approvals import RoleAssignmentApprovalsRequest
		return RoleAssignmentApprovalsRequest(self.request_adapter, path_parameters)

	def role_assignments(self,
		rbacApplication_id: str,
	) -> RoleAssignmentsRequest:
		if rbacApplication_id is None:
			raise TypeError("rbacApplication_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["rbacApplication%2Did"] =  rbacApplication_id

		from .role_assignments import RoleAssignmentsRequest
		return RoleAssignmentsRequest(self.request_adapter, path_parameters)

	def role_assignment_schedule_instances(self,
		rbacApplication_id: str,
	) -> RoleAssignmentScheduleInstancesRequest:
		if rbacApplication_id is None:
			raise TypeError("rbacApplication_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["rbacApplication%2Did"] =  rbacApplication_id

		from .role_assignment_schedule_instances import RoleAssignmentScheduleInstancesRequest
		return RoleAssignmentScheduleInstancesRequest(self.request_adapter, path_parameters)

	def role_assignment_schedule_requests(self,
		rbacApplication_id: str,
	) -> RoleAssignmentScheduleRequestsRequest:
		if rbacApplication_id is None:
			raise TypeError("rbacApplication_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["rbacApplication%2Did"] =  rbacApplication_id

		from .role_assignment_schedule_requests import RoleAssignmentScheduleRequestsRequest
		return RoleAssignmentScheduleRequestsRequest(self.request_adapter, path_parameters)

	def role_assignment_schedules(self,
		rbacApplication_id: str,
	) -> RoleAssignmentSchedulesRequest:
		if rbacApplication_id is None:
			raise TypeError("rbacApplication_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["rbacApplication%2Did"] =  rbacApplication_id

		from .role_assignment_schedules import RoleAssignmentSchedulesRequest
		return RoleAssignmentSchedulesRequest(self.request_adapter, path_parameters)

	def role_definitions(self,
		rbacApplication_id: str,
	) -> RoleDefinitionsRequest:
		if rbacApplication_id is None:
			raise TypeError("rbacApplication_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["rbacApplication%2Did"] =  rbacApplication_id

		from .role_definitions import RoleDefinitionsRequest
		return RoleDefinitionsRequest(self.request_adapter, path_parameters)

	def role_eligibility_schedule_instances(self,
		rbacApplication_id: str,
	) -> RoleEligibilityScheduleInstancesRequest:
		if rbacApplication_id is None:
			raise TypeError("rbacApplication_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["rbacApplication%2Did"] =  rbacApplication_id

		from .role_eligibility_schedule_instances import RoleEligibilityScheduleInstancesRequest
		return RoleEligibilityScheduleInstancesRequest(self.request_adapter, path_parameters)

	def role_eligibility_schedule_requests(self,
		rbacApplication_id: str,
	) -> RoleEligibilityScheduleRequestsRequest:
		if rbacApplication_id is None:
			raise TypeError("rbacApplication_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["rbacApplication%2Did"] =  rbacApplication_id

		from .role_eligibility_schedule_requests import RoleEligibilityScheduleRequestsRequest
		return RoleEligibilityScheduleRequestsRequest(self.request_adapter, path_parameters)

	def role_eligibility_schedules(self,
		rbacApplication_id: str,
	) -> RoleEligibilitySchedulesRequest:
		if rbacApplication_id is None:
			raise TypeError("rbacApplication_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["rbacApplication%2Did"] =  rbacApplication_id

		from .role_eligibility_schedules import RoleEligibilitySchedulesRequest
		return RoleEligibilitySchedulesRequest(self.request_adapter, path_parameters)

	def transitive_role_assignments(self,
		rbacApplication_id: str,
	) -> TransitiveRoleAssignmentsRequest:
		if rbacApplication_id is None:
			raise TypeError("rbacApplication_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["rbacApplication%2Did"] =  rbacApplication_id

		from .transitive_role_assignments import TransitiveRoleAssignmentsRequest
		return TransitiveRoleAssignmentsRequest(self.request_adapter, path_parameters)

