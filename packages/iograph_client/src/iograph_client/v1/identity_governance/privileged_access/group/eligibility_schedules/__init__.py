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
	from .by_privileged_access_group_eligibility_schedule_id import ByPrivilegedAccessGroupEligibilityScheduleIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
from iograph_models.v1.privileged_access_group_eligibility_schedule_collection_response import PrivilegedAccessGroupEligibilityScheduleCollectionResponse


class EligibilitySchedulesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/privilegedAccess/group/eligibilitySchedules", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrivilegedAccessGroupEligibilityScheduleCollectionResponse:
		"""
		List eligibilitySchedules
		Get a list of the privilegedAccessGroupEligibilitySchedule objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/privilegedaccessgroup-list-eligibilityschedules?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, PrivilegedAccessGroupEligibilityScheduleCollectionResponse, error_mapping)

	async def post(
		self,
		body: PrivilegedAccessGroupEligibilitySchedule,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrivilegedAccessGroupEligibilitySchedule:
		"""
		Create new navigation property to eligibilitySchedules for identityGovernance
		
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
		return await self.request_adapter.send_async(request_info, PrivilegedAccessGroupEligibilitySchedule, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> EligibilitySchedulesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: EligibilitySchedulesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return EligibilitySchedulesRequest(self.request_adapter, self.path_parameters)

	def by_privileged_access_group_eligibility_schedule_id(self,
		privilegedAccessGroupEligibilitySchedule_id: str,
	) -> ByPrivilegedAccessGroupEligibilityScheduleIdRequest:
		if privilegedAccessGroupEligibilitySchedule_id is None:
			raise TypeError("privilegedAccessGroupEligibilitySchedule_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccessGroupEligibilitySchedule%2Did"] =  privilegedAccessGroupEligibilitySchedule_id

		from .by_privileged_access_group_eligibility_schedule_id import ByPrivilegedAccessGroupEligibilityScheduleIdRequest
		return ByPrivilegedAccessGroupEligibilityScheduleIdRequest(self.request_adapter, path_parameters)

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

