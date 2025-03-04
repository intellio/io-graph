# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .delta import DeltaRequest
	from .count import CountRequest
	from .by_event_id import ByEventIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.event_collection_response import EventCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.event import Event


class EventsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/calendarGroups/{calendarGroup%2Did}/calendars/{calendar%2Did}/events", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EventCollectionResponse:
		"""
		Get events from me
		The events in the calendar. Navigation property. Read-only.
		"""
		tags = ['me.calendarGroup']

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
		return await self.request_adapter.send_async(request_info, EventCollectionResponse, error_mapping)

	async def post(
		self,
		body: Event,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Event:
		"""
		Create new navigation property to events for me
		
		"""
		tags = ['me.calendarGroup']

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
		return await self.request_adapter.send_async(request_info, Event, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> EventsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: EventsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return EventsRequest(self.request_adapter, self.path_parameters)

	def by_event_id(self,
		calendarGroup_id: str,
		calendar_id: str,
		event_id: str,
	) -> ByEventIdRequest:
		if calendarGroup_id is None:
			raise TypeError("calendarGroup_id cannot be null.")
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["calendarGroup%2Did"] =  calendarGroup_id
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id

		from .by_event_id import ByEventIdRequest
		return ByEventIdRequest(self.request_adapter, path_parameters)

	def count(self,
		calendarGroup_id: str,
		calendar_id: str,
	) -> CountRequest:
		if calendarGroup_id is None:
			raise TypeError("calendarGroup_id cannot be null.")
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["calendarGroup%2Did"] =  calendarGroup_id
		path_parameters["calendar%2Did"] =  calendar_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def delta(self,
		calendarGroup_id: str,
		calendar_id: str,
	) -> DeltaRequest:
		if calendarGroup_id is None:
			raise TypeError("calendarGroup_id cannot be null.")
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["calendarGroup%2Did"] =  calendarGroup_id
		path_parameters["calendar%2Did"] =  calendar_id

		from .delta import DeltaRequest
		return DeltaRequest(self.request_adapter, path_parameters)

