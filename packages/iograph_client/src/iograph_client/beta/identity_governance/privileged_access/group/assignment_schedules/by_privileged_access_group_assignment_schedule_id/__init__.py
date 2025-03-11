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
	from .principal import PrincipalRequest
	from .group import GroupRequest
	from .activated_using import ActivatedUsingRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByPrivilegedAccessGroupAssignmentScheduleIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/privilegedAccess/group/assignmentSchedules/{privilegedAccessGroupAssignmentSchedule%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrivilegedAccessGroupAssignmentSchedule:
		"""
		Get privilegedAccessGroupAssignmentSchedule
		Read the properties and relationships of a privilegedAccessGroupAssignmentSchedule object.
		Find more info here: https://learn.microsoft.com/graph/api/privilegedaccessgroupassignmentschedule-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, PrivilegedAccessGroupAssignmentSchedule, error_mapping)

	async def patch(
		self,
		body: PrivilegedAccessGroupAssignmentSchedule,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrivilegedAccessGroupAssignmentSchedule:
		"""
		Update the navigation property assignmentSchedules in identityGovernance
		
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
		return await self.request_adapter.send_async(request_info, PrivilegedAccessGroupAssignmentSchedule, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property assignmentSchedules for identityGovernance
		
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



	def with_url(self, raw_url: str) -> ByPrivilegedAccessGroupAssignmentScheduleIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPrivilegedAccessGroupAssignmentScheduleIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPrivilegedAccessGroupAssignmentScheduleIdRequest(self.request_adapter, self.path_parameters)

	def activated_using(self,
		privilegedAccessGroupAssignmentSchedule_id: str,
	) -> ActivatedUsingRequest:
		if privilegedAccessGroupAssignmentSchedule_id is None:
			raise TypeError("privilegedAccessGroupAssignmentSchedule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccessGroupAssignmentSchedule%2Did"] =  privilegedAccessGroupAssignmentSchedule_id

		from .activated_using import ActivatedUsingRequest
		return ActivatedUsingRequest(self.request_adapter, path_parameters)

	def group(self,
		privilegedAccessGroupAssignmentSchedule_id: str,
	) -> GroupRequest:
		if privilegedAccessGroupAssignmentSchedule_id is None:
			raise TypeError("privilegedAccessGroupAssignmentSchedule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccessGroupAssignmentSchedule%2Did"] =  privilegedAccessGroupAssignmentSchedule_id

		from .group import GroupRequest
		return GroupRequest(self.request_adapter, path_parameters)

	def principal(self,
		privilegedAccessGroupAssignmentSchedule_id: str,
	) -> PrincipalRequest:
		if privilegedAccessGroupAssignmentSchedule_id is None:
			raise TypeError("privilegedAccessGroupAssignmentSchedule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccessGroupAssignmentSchedule%2Did"] =  privilegedAccessGroupAssignmentSchedule_id

		from .principal import PrincipalRequest
		return PrincipalRequest(self.request_adapter, path_parameters)

