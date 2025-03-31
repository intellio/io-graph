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
	from .filter_by_current_user_with_on import FilterByCurrentUserWithOnRequest
	from .count import CountRequest
	from .by_privileged_access_group_eligibility_schedule_request_id import ByPrivilegedAccessGroupEligibilityScheduleRequestIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.privileged_access_group_eligibility_schedule_request_collection_response import PrivilegedAccessGroupEligibilityScheduleRequestCollectionResponse
from iograph_models.v1.privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class EligibilityScheduleRequestsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/privilegedAccess/group/eligibilityScheduleRequests", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrivilegedAccessGroupEligibilityScheduleRequestCollectionResponse:
		"""
		List eligibilityScheduleRequests
		Get a list of the privilegedAccessGroupEligibilityScheduleRequest objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/privilegedaccessgroup-list-eligibilityschedulerequests?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, PrivilegedAccessGroupEligibilityScheduleRequestCollectionResponse, error_mapping)

	async def post(
		self,
		body: PrivilegedAccessGroupEligibilityScheduleRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrivilegedAccessGroupEligibilityScheduleRequest:
		"""
		Create eligibilityScheduleRequest
		Create a new privilegedAccessGroupEligibilityScheduleRequest object.
		Find more info here: https://learn.microsoft.com/graph/api/privilegedaccessgroup-post-eligibilityschedulerequests?view=graph-rest-1.0
		"""
		tags = ['identityGovernance.privilegedAccessRoot']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, PrivilegedAccessGroupEligibilityScheduleRequest, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> EligibilityScheduleRequestsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: EligibilityScheduleRequestsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return EligibilityScheduleRequestsRequest(self.request_adapter, self.path_parameters)

	def by_privileged_access_group_eligibility_schedule_request_id(self,
		privilegedAccessGroupEligibilityScheduleRequest_id: str,
	) -> ByPrivilegedAccessGroupEligibilityScheduleRequestIdRequest:
		if privilegedAccessGroupEligibilityScheduleRequest_id is None:
			raise TypeError("privilegedAccessGroupEligibilityScheduleRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccessGroupEligibilityScheduleRequest%2Did"] =  privilegedAccessGroupEligibilityScheduleRequest_id

		from .by_privileged_access_group_eligibility_schedule_request_id import ByPrivilegedAccessGroupEligibilityScheduleRequestIdRequest
		return ByPrivilegedAccessGroupEligibilityScheduleRequestIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	def filter_by_current_user_with_on(self,
		on: str,
	) -> FilterByCurrentUserWithOnRequest:
		if on is None:
			raise TypeError("on cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["on"] =  on

		from .filter_by_current_user_with_on import FilterByCurrentUserWithOnRequest
		return FilterByCurrentUserWithOnRequest(self.request_adapter, path_parameters)

