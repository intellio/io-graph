# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .eligibility_schedules import EligibilitySchedulesRequest
	from .eligibility_schedule_requests import EligibilityScheduleRequestsRequest
	from .eligibility_schedule_instances import EligibilityScheduleInstancesRequest
	from .assignment_schedules import AssignmentSchedulesRequest
	from .assignment_schedule_requests import AssignmentScheduleRequestsRequest
	from .assignment_schedule_instances import AssignmentScheduleInstancesRequest
	from .assignment_approvals import AssignmentApprovalsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.privileged_access_group import PrivilegedAccessGroup
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class GroupRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/privilegedAccess/group", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrivilegedAccessGroup:
		"""
		Get group from identityGovernance
		A group that's governed through Privileged Identity Management (PIM).
		"""
		tags = ['identityGovernance.privilegedAccessRoot']

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
		return await self.request_adapter.send_async(request_info, PrivilegedAccessGroup, error_mapping)

	async def patch(
		self,
		body: PrivilegedAccessGroup,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrivilegedAccessGroup:
		"""
		Update the navigation property group in identityGovernance
		
		"""
		tags = ['identityGovernance.privilegedAccessRoot']

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
		return await self.request_adapter.send_async(request_info, PrivilegedAccessGroup, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property group for identityGovernance
		
		"""
		tags = ['identityGovernance.privilegedAccessRoot']
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



	def with_url(self, raw_url: str) -> GroupRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GroupRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GroupRequest(self.request_adapter, self.path_parameters)

	@property
	def assignment_approvals(self,
	) -> AssignmentApprovalsRequest:
		from .assignment_approvals import AssignmentApprovalsRequest
		return AssignmentApprovalsRequest(self.request_adapter, self.path_parameters)

	@property
	def assignment_schedule_instances(self,
	) -> AssignmentScheduleInstancesRequest:
		from .assignment_schedule_instances import AssignmentScheduleInstancesRequest
		return AssignmentScheduleInstancesRequest(self.request_adapter, self.path_parameters)

	@property
	def assignment_schedule_requests(self,
	) -> AssignmentScheduleRequestsRequest:
		from .assignment_schedule_requests import AssignmentScheduleRequestsRequest
		return AssignmentScheduleRequestsRequest(self.request_adapter, self.path_parameters)

	@property
	def assignment_schedules(self,
	) -> AssignmentSchedulesRequest:
		from .assignment_schedules import AssignmentSchedulesRequest
		return AssignmentSchedulesRequest(self.request_adapter, self.path_parameters)

	@property
	def eligibility_schedule_instances(self,
	) -> EligibilityScheduleInstancesRequest:
		from .eligibility_schedule_instances import EligibilityScheduleInstancesRequest
		return EligibilityScheduleInstancesRequest(self.request_adapter, self.path_parameters)

	@property
	def eligibility_schedule_requests(self,
	) -> EligibilityScheduleRequestsRequest:
		from .eligibility_schedule_requests import EligibilityScheduleRequestsRequest
		return EligibilityScheduleRequestsRequest(self.request_adapter, self.path_parameters)

	@property
	def eligibility_schedules(self,
	) -> EligibilitySchedulesRequest:
		from .eligibility_schedules import EligibilitySchedulesRequest
		return EligibilitySchedulesRequest(self.request_adapter, self.path_parameters)

