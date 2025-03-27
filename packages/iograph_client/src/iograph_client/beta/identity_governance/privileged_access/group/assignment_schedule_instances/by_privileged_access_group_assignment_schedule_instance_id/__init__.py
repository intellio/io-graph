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
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance


class ByPrivilegedAccessGroupAssignmentScheduleInstanceIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/privilegedAccess/group/assignmentScheduleInstances/{privilegedAccessGroupAssignmentScheduleInstance%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrivilegedAccessGroupAssignmentScheduleInstance:
		"""
		Get privilegedAccessGroupAssignmentScheduleInstance
		Read the properties and relationships of a privilegedAccessGroupAssignmentScheduleInstance object.
		Find more info here: https://learn.microsoft.com/graph/api/privilegedaccessgroupassignmentscheduleinstance-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, PrivilegedAccessGroupAssignmentScheduleInstance, error_mapping)

	async def patch(
		self,
		body: PrivilegedAccessGroupAssignmentScheduleInstance,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrivilegedAccessGroupAssignmentScheduleInstance:
		"""
		Update the navigation property assignmentScheduleInstances in identityGovernance
		
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
		return await self.request_adapter.send_async(request_info, PrivilegedAccessGroupAssignmentScheduleInstance, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property assignmentScheduleInstances for identityGovernance
		
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



	def with_url(self, raw_url: str) -> ByPrivilegedAccessGroupAssignmentScheduleInstanceIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPrivilegedAccessGroupAssignmentScheduleInstanceIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPrivilegedAccessGroupAssignmentScheduleInstanceIdRequest(self.request_adapter, self.path_parameters)

	def activated_using(self,
		privilegedAccessGroupAssignmentScheduleInstance_id: str,
	) -> ActivatedUsingRequest:
		if privilegedAccessGroupAssignmentScheduleInstance_id is None:
			raise TypeError("privilegedAccessGroupAssignmentScheduleInstance_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccessGroupAssignmentScheduleInstance%2Did"] =  privilegedAccessGroupAssignmentScheduleInstance_id

		from .activated_using import ActivatedUsingRequest
		return ActivatedUsingRequest(self.request_adapter, path_parameters)

	def group(self,
		privilegedAccessGroupAssignmentScheduleInstance_id: str,
	) -> GroupRequest:
		if privilegedAccessGroupAssignmentScheduleInstance_id is None:
			raise TypeError("privilegedAccessGroupAssignmentScheduleInstance_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccessGroupAssignmentScheduleInstance%2Did"] =  privilegedAccessGroupAssignmentScheduleInstance_id

		from .group import GroupRequest
		return GroupRequest(self.request_adapter, path_parameters)

	def principal(self,
		privilegedAccessGroupAssignmentScheduleInstance_id: str,
	) -> PrincipalRequest:
		if privilegedAccessGroupAssignmentScheduleInstance_id is None:
			raise TypeError("privilegedAccessGroupAssignmentScheduleInstance_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccessGroupAssignmentScheduleInstance%2Did"] =  privilegedAccessGroupAssignmentScheduleInstance_id

		from .principal import PrincipalRequest
		return PrincipalRequest(self.request_adapter, path_parameters)

