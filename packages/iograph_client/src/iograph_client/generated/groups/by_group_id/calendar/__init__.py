# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .get_schedule import GetScheduleRequest
	from .allowed_calendar_sharing_roles_with_user import AllowedCalendarSharingRolesWithUserRequest
	from .events import EventsRequest
	from .calendar_view import CalendarViewRequest
	from .calendar_permissions import CalendarPermissionsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.calendar import Calendar


class CalendarRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/calendar", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Calendar:
		"""
		Get calendar from groups
		The group's calendar. Read-only.
		"""
		tags = ['groups.calendar']

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

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> CalendarRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CalendarRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CalendarRequest(self.request_adapter, self.path_parameters)

	def calendar_permissions(self,
		group_id: str,
	) -> CalendarPermissionsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .calendar_permissions import CalendarPermissionsRequest
		return CalendarPermissionsRequest(self.request_adapter, path_parameters)

	def calendar_view(self,
		group_id: str,
	) -> CalendarViewRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .calendar_view import CalendarViewRequest
		return CalendarViewRequest(self.request_adapter, path_parameters)

	def events(self,
		group_id: str,
	) -> EventsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .events import EventsRequest
		return EventsRequest(self.request_adapter, path_parameters)

	def allowed_calendar_sharing_roles_with_user(self,
		group_id: str,
		User: str,
	) -> AllowedCalendarSharingRolesWithUserRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if User is None:
			raise TypeError("User cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["User"] =  User

		from .allowed_calendar_sharing_roles_with_user import AllowedCalendarSharingRolesWithUserRequest
		return AllowedCalendarSharingRolesWithUserRequest(self.request_adapter, path_parameters)

	def get_schedule(self,
		group_id: str,
	) -> GetScheduleRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id

		from .get_schedule import GetScheduleRequest
		return GetScheduleRequest(self.request_adapter, path_parameters)

