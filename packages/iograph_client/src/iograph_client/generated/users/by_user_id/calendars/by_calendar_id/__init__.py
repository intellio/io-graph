# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .get_schedule import GetScheduleRequest
	from .events import EventsRequest
	from .calendar_view import CalendarViewRequest
	from .calendar_permissions import CalendarPermissionsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.calendar import Calendar


class ByCalendarIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/users/{user%2Did}/calendars/{calendar%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Calendar:
		"""
		Get calendars from users
		The user's calendars. Read-only. Nullable.
		"""
		tags = ['users.calendar']

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
		return await self.request_adapter.send_async(request_info, Calendar, error_mapping)

	async def patch(
		self,
		body: Calendar,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Calendar:
		"""
		Update the navigation property calendars in users
		
		"""
		tags = ['users.calendar']

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
		return await self.request_adapter.send_async(request_info, Calendar, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property calendars for users
		
		"""
		tags = ['users.calendar']
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



	@property
	def calendar_permissions(self,
	) -> CalendarPermissionsRequest:
		from .calendar_permissions import CalendarPermissionsRequest
		return CalendarPermissionsRequest(self.request_adapter, self.path_parameters)

	@property
	def calendar_view(self,
	) -> CalendarViewRequest:
		from .calendar_view import CalendarViewRequest
		return CalendarViewRequest(self.request_adapter, self.path_parameters)

	@property
	def events(self,
	) -> EventsRequest:
		from .events import EventsRequest
		return EventsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_schedule(self,
	) -> GetScheduleRequest:
		from .get_schedule import GetScheduleRequest
		return GetScheduleRequest(self.request_adapter, self.path_parameters)

