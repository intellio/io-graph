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
	from .target_schedule import TargetScheduleRequest
	from .principal import PrincipalRequest
	from .cancel import CancelRequest
	from .group import GroupRequest
	from .activated_using import ActivatedUsingRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByPrivilegedAccessGroupAssignmentScheduleRequestIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/privilegedAccess/group/assignmentScheduleRequests/{privilegedAccessGroupAssignmentScheduleRequest%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrivilegedAccessGroupAssignmentScheduleRequest:
		"""
		Get privilegedAccessGroupAssignmentScheduleRequest
		Read the properties and relationships of a privilegedAccessGroupAssignmentScheduleRequest object.
		Find more info here: https://learn.microsoft.com/graph/api/privilegedaccessgroupassignmentschedulerequest-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, PrivilegedAccessGroupAssignmentScheduleRequest, error_mapping)

	async def patch(
		self,
		body: PrivilegedAccessGroupAssignmentScheduleRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrivilegedAccessGroupAssignmentScheduleRequest:
		"""
		Update the navigation property assignmentScheduleRequests in identityGovernance
		
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
		return await self.request_adapter.send_async(request_info, PrivilegedAccessGroupAssignmentScheduleRequest, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property assignmentScheduleRequests for identityGovernance
		
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



	def with_url(self, raw_url: str) -> ByPrivilegedAccessGroupAssignmentScheduleRequestIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPrivilegedAccessGroupAssignmentScheduleRequestIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPrivilegedAccessGroupAssignmentScheduleRequestIdRequest(self.request_adapter, self.path_parameters)

	def activated_using(self,
		privilegedAccessGroupAssignmentScheduleRequest_id: str,
	) -> ActivatedUsingRequest:
		if privilegedAccessGroupAssignmentScheduleRequest_id is None:
			raise TypeError("privilegedAccessGroupAssignmentScheduleRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccessGroupAssignmentScheduleRequest%2Did"] =  privilegedAccessGroupAssignmentScheduleRequest_id

		from .activated_using import ActivatedUsingRequest
		return ActivatedUsingRequest(self.request_adapter, path_parameters)

	def group(self,
		privilegedAccessGroupAssignmentScheduleRequest_id: str,
	) -> GroupRequest:
		if privilegedAccessGroupAssignmentScheduleRequest_id is None:
			raise TypeError("privilegedAccessGroupAssignmentScheduleRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccessGroupAssignmentScheduleRequest%2Did"] =  privilegedAccessGroupAssignmentScheduleRequest_id

		from .group import GroupRequest
		return GroupRequest(self.request_adapter, path_parameters)

	def cancel(self,
		privilegedAccessGroupAssignmentScheduleRequest_id: str,
	) -> CancelRequest:
		if privilegedAccessGroupAssignmentScheduleRequest_id is None:
			raise TypeError("privilegedAccessGroupAssignmentScheduleRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccessGroupAssignmentScheduleRequest%2Did"] =  privilegedAccessGroupAssignmentScheduleRequest_id

		from .cancel import CancelRequest
		return CancelRequest(self.request_adapter, path_parameters)

	def principal(self,
		privilegedAccessGroupAssignmentScheduleRequest_id: str,
	) -> PrincipalRequest:
		if privilegedAccessGroupAssignmentScheduleRequest_id is None:
			raise TypeError("privilegedAccessGroupAssignmentScheduleRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccessGroupAssignmentScheduleRequest%2Did"] =  privilegedAccessGroupAssignmentScheduleRequest_id

		from .principal import PrincipalRequest
		return PrincipalRequest(self.request_adapter, path_parameters)

	def target_schedule(self,
		privilegedAccessGroupAssignmentScheduleRequest_id: str,
	) -> TargetScheduleRequest:
		if privilegedAccessGroupAssignmentScheduleRequest_id is None:
			raise TypeError("privilegedAccessGroupAssignmentScheduleRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccessGroupAssignmentScheduleRequest%2Did"] =  privilegedAccessGroupAssignmentScheduleRequest_id

		from .target_schedule import TargetScheduleRequest
		return TargetScheduleRequest(self.request_adapter, path_parameters)

