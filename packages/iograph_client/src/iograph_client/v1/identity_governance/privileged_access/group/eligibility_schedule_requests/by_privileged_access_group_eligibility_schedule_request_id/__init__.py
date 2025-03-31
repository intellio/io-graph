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
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByPrivilegedAccessGroupEligibilityScheduleRequestIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/privilegedAccess/group/eligibilityScheduleRequests/{privilegedAccessGroupEligibilityScheduleRequest%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrivilegedAccessGroupEligibilityScheduleRequest:
		"""
		Get privilegedAccessGroupEligibilityScheduleRequest
		Read the properties and relationships of a privilegedAccessGroupEligibilityScheduleRequest object.
		Find more info here: https://learn.microsoft.com/graph/api/privilegedaccessgroupeligibilityschedulerequest-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, PrivilegedAccessGroupEligibilityScheduleRequest, error_mapping)

	async def patch(
		self,
		body: PrivilegedAccessGroupEligibilityScheduleRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrivilegedAccessGroupEligibilityScheduleRequest:
		"""
		Update the navigation property eligibilityScheduleRequests in identityGovernance
		
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
		return await self.request_adapter.send_async(request_info, PrivilegedAccessGroupEligibilityScheduleRequest, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property eligibilityScheduleRequests for identityGovernance
		
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



	def with_url(self, raw_url: str) -> ByPrivilegedAccessGroupEligibilityScheduleRequestIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPrivilegedAccessGroupEligibilityScheduleRequestIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPrivilegedAccessGroupEligibilityScheduleRequestIdRequest(self.request_adapter, self.path_parameters)

	def group(self,
		privilegedAccessGroupEligibilityScheduleRequest_id: str,
	) -> GroupRequest:
		if privilegedAccessGroupEligibilityScheduleRequest_id is None:
			raise TypeError("privilegedAccessGroupEligibilityScheduleRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccessGroupEligibilityScheduleRequest%2Did"] =  privilegedAccessGroupEligibilityScheduleRequest_id

		from .group import GroupRequest
		return GroupRequest(self.request_adapter, path_parameters)

	def cancel(self,
		privilegedAccessGroupEligibilityScheduleRequest_id: str,
	) -> CancelRequest:
		if privilegedAccessGroupEligibilityScheduleRequest_id is None:
			raise TypeError("privilegedAccessGroupEligibilityScheduleRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccessGroupEligibilityScheduleRequest%2Did"] =  privilegedAccessGroupEligibilityScheduleRequest_id

		from .cancel import CancelRequest
		return CancelRequest(self.request_adapter, path_parameters)

	def principal(self,
		privilegedAccessGroupEligibilityScheduleRequest_id: str,
	) -> PrincipalRequest:
		if privilegedAccessGroupEligibilityScheduleRequest_id is None:
			raise TypeError("privilegedAccessGroupEligibilityScheduleRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccessGroupEligibilityScheduleRequest%2Did"] =  privilegedAccessGroupEligibilityScheduleRequest_id

		from .principal import PrincipalRequest
		return PrincipalRequest(self.request_adapter, path_parameters)

	def target_schedule(self,
		privilegedAccessGroupEligibilityScheduleRequest_id: str,
	) -> TargetScheduleRequest:
		if privilegedAccessGroupEligibilityScheduleRequest_id is None:
			raise TypeError("privilegedAccessGroupEligibilityScheduleRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccessGroupEligibilityScheduleRequest%2Did"] =  privilegedAccessGroupEligibilityScheduleRequest_id

		from .target_schedule import TargetScheduleRequest
		return TargetScheduleRequest(self.request_adapter, path_parameters)

