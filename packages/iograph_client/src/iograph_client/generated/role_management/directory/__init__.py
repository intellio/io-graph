# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .role_eligibility_schedules import RoleEligibilitySchedulesRequest
	from .role_eligibility_schedule_requests import RoleEligibilityScheduleRequestsRequest
	from .role_eligibility_schedule_instances import RoleEligibilityScheduleInstancesRequest
	from .role_definitions import RoleDefinitionsRequest
	from .role_assignment_schedules import RoleAssignmentSchedulesRequest
	from .role_assignment_schedule_requests import RoleAssignmentScheduleRequestsRequest
	from .role_assignment_schedule_instances import RoleAssignmentScheduleInstancesRequest
	from .role_assignments import RoleAssignmentsRequest
	from .resource_namespaces import ResourceNamespacesRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.rbac_application import RbacApplication


class DirectoryRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/roleManagement/directory"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> RbacApplication:
		"""
		Get directory from roleManagement
		
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
		Update the navigation property directory in roleManagement
		
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
		Delete navigation property directory for roleManagement
		
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



	@property
	def resource_namespaces(self,
	) -> ResourceNamespacesRequest:
		from .resource_namespaces import ResourceNamespacesRequest
		return ResourceNamespacesRequest(self.request_adapter, self.path_parameters)

	@property
	def role_assignments(self,
	) -> RoleAssignmentsRequest:
		from .role_assignments import RoleAssignmentsRequest
		return RoleAssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def role_assignment_schedule_instances(self,
	) -> RoleAssignmentScheduleInstancesRequest:
		from .role_assignment_schedule_instances import RoleAssignmentScheduleInstancesRequest
		return RoleAssignmentScheduleInstancesRequest(self.request_adapter, self.path_parameters)

	@property
	def role_assignment_schedule_requests(self,
	) -> RoleAssignmentScheduleRequestsRequest:
		from .role_assignment_schedule_requests import RoleAssignmentScheduleRequestsRequest
		return RoleAssignmentScheduleRequestsRequest(self.request_adapter, self.path_parameters)

	@property
	def role_assignment_schedules(self,
	) -> RoleAssignmentSchedulesRequest:
		from .role_assignment_schedules import RoleAssignmentSchedulesRequest
		return RoleAssignmentSchedulesRequest(self.request_adapter, self.path_parameters)

	@property
	def role_definitions(self,
	) -> RoleDefinitionsRequest:
		from .role_definitions import RoleDefinitionsRequest
		return RoleDefinitionsRequest(self.request_adapter, self.path_parameters)

	@property
	def role_eligibility_schedule_instances(self,
	) -> RoleEligibilityScheduleInstancesRequest:
		from .role_eligibility_schedule_instances import RoleEligibilityScheduleInstancesRequest
		return RoleEligibilityScheduleInstancesRequest(self.request_adapter, self.path_parameters)

	@property
	def role_eligibility_schedule_requests(self,
	) -> RoleEligibilityScheduleRequestsRequest:
		from .role_eligibility_schedule_requests import RoleEligibilityScheduleRequestsRequest
		return RoleEligibilityScheduleRequestsRequest(self.request_adapter, self.path_parameters)

	@property
	def role_eligibility_schedules(self,
	) -> RoleEligibilitySchedulesRequest:
		from .role_eligibility_schedules import RoleEligibilitySchedulesRequest
		return RoleEligibilitySchedulesRequest(self.request_adapter, self.path_parameters)

