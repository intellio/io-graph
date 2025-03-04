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
	from .count import CountRequest
	from .by_time_off_request_id import ByTimeOffRequestIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.time_off_request import TimeOffRequest
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.time_off_request_collection_response import TimeOffRequestCollectionResponse


class TimeOffRequestsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/joinedTeams/{team%2Did}/schedule/timeOffRequests", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TimeOffRequestCollectionResponse:
		"""
		Get timeOffRequests from me
		The time off requests in the schedule.
		"""
		tags = ['me.team']

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
		return await self.request_adapter.send_async(request_info, TimeOffRequestCollectionResponse, error_mapping)

	async def post(
		self,
		body: TimeOffRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TimeOffRequest:
		"""
		Create new navigation property to timeOffRequests for me
		
		"""
		tags = ['me.team']

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
		return await self.request_adapter.send_async(request_info, TimeOffRequest, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> TimeOffRequestsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: TimeOffRequestsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return TimeOffRequestsRequest(self.request_adapter, self.path_parameters)

	def by_time_off_request_id(self,
		team_id: str,
		timeOffRequest_id: str,
	) -> ByTimeOffRequestIdRequest:
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if timeOffRequest_id is None:
			raise TypeError("timeOffRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["team%2Did"] =  team_id
		path_parameters["timeOffRequest%2Did"] =  timeOffRequest_id

		from .by_time_off_request_id import ByTimeOffRequestIdRequest
		return ByTimeOffRequestIdRequest(self.request_adapter, path_parameters)

	def count(self,
		team_id: str,
	) -> CountRequest:
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["team%2Did"] =  team_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

