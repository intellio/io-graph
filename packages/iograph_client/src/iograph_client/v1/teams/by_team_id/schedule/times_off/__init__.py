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
	from .count import CountRequest
	from .by_time_off_id import ByTimeOffIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.time_off import TimeOff
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.time_off_collection_response import TimeOffCollectionResponse


class TimesOffRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/teams/{team%2Did}/schedule/timesOff", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TimeOffCollectionResponse:
		"""
		List timesOff
		Get the list of timeOff instances in a schedule.
		Find more info here: https://learn.microsoft.com/graph/api/schedule-list-timesoff?view=graph-rest-1.0
		"""
		tags = ['teams.schedule']

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
		return await self.request_adapter.send_async(request_info, TimeOffCollectionResponse, error_mapping)

	async def post(
		self,
		body: TimeOff,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TimeOff:
		"""
		Create timeOff
		Create a new timeOff instance in a schedule.
		Find more info here: https://learn.microsoft.com/graph/api/schedule-post-timesoff?view=graph-rest-1.0
		"""
		tags = ['teams.schedule']

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
		return await self.request_adapter.send_async(request_info, TimeOff, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> TimesOffRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: TimesOffRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return TimesOffRequest(self.request_adapter, self.path_parameters)

	def by_time_off_id(self,
		team_id: str,
		timeOff_id: str,
	) -> ByTimeOffIdRequest:
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if timeOff_id is None:
			raise TypeError("timeOff_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["team%2Did"] =  team_id
		path_parameters["timeOff%2Did"] =  timeOff_id

		from .by_time_off_id import ByTimeOffIdRequest
		return ByTimeOffIdRequest(self.request_adapter, path_parameters)

	def count(self,
		team_id: str,
	) -> CountRequest:
		if team_id is None:
			raise TypeError("team_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["team%2Did"] =  team_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

