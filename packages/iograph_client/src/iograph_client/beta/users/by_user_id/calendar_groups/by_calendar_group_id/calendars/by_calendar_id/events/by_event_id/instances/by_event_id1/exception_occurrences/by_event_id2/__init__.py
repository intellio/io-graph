# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..............request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .tentatively_accept import TentativelyAcceptRequest
	from .snooze_reminder import SnoozeReminderRequest
	from .permanent_delete import PermanentDeleteRequest
	from .forward import ForwardRequest
	from .dismiss_reminder import DismissReminderRequest
	from .decline import DeclineRequest
	from .cancel import CancelRequest
	from .accept import AcceptRequest
	from .extensions import ExtensionsRequest
	from .calendar import CalendarRequest
	from .attachments import AttachmentsRequest
	from ..............request_adapter import HttpxRequestAdapter
from iograph_models.beta.event import Event
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByEventId2Request(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/calendarGroups/{calendarGroup%2Did}/calendars/{calendar%2Did}/events/{event%2Did}/instances/{event%2Did1}/exceptionOccurrences/{event%2Did2}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Event:
		"""
		Get exceptionOccurrences from users
		
		"""
		tags = ['users.calendarGroup']

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
		return await self.request_adapter.send_async(request_info, Event, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ByEventId2Request:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByEventId2Request
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByEventId2Request(self.request_adapter, self.path_parameters)

	def attachments(self,
		user_id: str,
		calendarGroup_id: str,
		calendar_id: str,
		event_id: str,
		event_id1: str,
		event_id2: str,
	) -> AttachmentsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if calendarGroup_id is None:
			raise TypeError("calendarGroup_id cannot be null.")
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")
		if event_id2 is None:
			raise TypeError("event_id2 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["calendarGroup%2Did"] =  calendarGroup_id
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1
		path_parameters["event%2Did2"] =  event_id2

		from .attachments import AttachmentsRequest
		return AttachmentsRequest(self.request_adapter, path_parameters)

	def calendar(self,
		user_id: str,
		calendarGroup_id: str,
		calendar_id: str,
		event_id: str,
		event_id1: str,
		event_id2: str,
	) -> CalendarRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if calendarGroup_id is None:
			raise TypeError("calendarGroup_id cannot be null.")
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")
		if event_id2 is None:
			raise TypeError("event_id2 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["calendarGroup%2Did"] =  calendarGroup_id
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1
		path_parameters["event%2Did2"] =  event_id2

		from .calendar import CalendarRequest
		return CalendarRequest(self.request_adapter, path_parameters)

	def extensions(self,
		user_id: str,
		calendarGroup_id: str,
		calendar_id: str,
		event_id: str,
		event_id1: str,
		event_id2: str,
	) -> ExtensionsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if calendarGroup_id is None:
			raise TypeError("calendarGroup_id cannot be null.")
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")
		if event_id2 is None:
			raise TypeError("event_id2 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["calendarGroup%2Did"] =  calendarGroup_id
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1
		path_parameters["event%2Did2"] =  event_id2

		from .extensions import ExtensionsRequest
		return ExtensionsRequest(self.request_adapter, path_parameters)

	def accept(self,
		user_id: str,
		calendarGroup_id: str,
		calendar_id: str,
		event_id: str,
		event_id1: str,
		event_id2: str,
	) -> AcceptRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if calendarGroup_id is None:
			raise TypeError("calendarGroup_id cannot be null.")
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")
		if event_id2 is None:
			raise TypeError("event_id2 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["calendarGroup%2Did"] =  calendarGroup_id
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1
		path_parameters["event%2Did2"] =  event_id2

		from .accept import AcceptRequest
		return AcceptRequest(self.request_adapter, path_parameters)

	def cancel(self,
		user_id: str,
		calendarGroup_id: str,
		calendar_id: str,
		event_id: str,
		event_id1: str,
		event_id2: str,
	) -> CancelRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if calendarGroup_id is None:
			raise TypeError("calendarGroup_id cannot be null.")
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")
		if event_id2 is None:
			raise TypeError("event_id2 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["calendarGroup%2Did"] =  calendarGroup_id
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1
		path_parameters["event%2Did2"] =  event_id2

		from .cancel import CancelRequest
		return CancelRequest(self.request_adapter, path_parameters)

	def decline(self,
		user_id: str,
		calendarGroup_id: str,
		calendar_id: str,
		event_id: str,
		event_id1: str,
		event_id2: str,
	) -> DeclineRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if calendarGroup_id is None:
			raise TypeError("calendarGroup_id cannot be null.")
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")
		if event_id2 is None:
			raise TypeError("event_id2 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["calendarGroup%2Did"] =  calendarGroup_id
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1
		path_parameters["event%2Did2"] =  event_id2

		from .decline import DeclineRequest
		return DeclineRequest(self.request_adapter, path_parameters)

	def dismiss_reminder(self,
		user_id: str,
		calendarGroup_id: str,
		calendar_id: str,
		event_id: str,
		event_id1: str,
		event_id2: str,
	) -> DismissReminderRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if calendarGroup_id is None:
			raise TypeError("calendarGroup_id cannot be null.")
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")
		if event_id2 is None:
			raise TypeError("event_id2 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["calendarGroup%2Did"] =  calendarGroup_id
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1
		path_parameters["event%2Did2"] =  event_id2

		from .dismiss_reminder import DismissReminderRequest
		return DismissReminderRequest(self.request_adapter, path_parameters)

	def forward(self,
		user_id: str,
		calendarGroup_id: str,
		calendar_id: str,
		event_id: str,
		event_id1: str,
		event_id2: str,
	) -> ForwardRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if calendarGroup_id is None:
			raise TypeError("calendarGroup_id cannot be null.")
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")
		if event_id2 is None:
			raise TypeError("event_id2 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["calendarGroup%2Did"] =  calendarGroup_id
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1
		path_parameters["event%2Did2"] =  event_id2

		from .forward import ForwardRequest
		return ForwardRequest(self.request_adapter, path_parameters)

	def permanent_delete(self,
		user_id: str,
		calendarGroup_id: str,
		calendar_id: str,
		event_id: str,
		event_id1: str,
		event_id2: str,
	) -> PermanentDeleteRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if calendarGroup_id is None:
			raise TypeError("calendarGroup_id cannot be null.")
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")
		if event_id2 is None:
			raise TypeError("event_id2 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["calendarGroup%2Did"] =  calendarGroup_id
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1
		path_parameters["event%2Did2"] =  event_id2

		from .permanent_delete import PermanentDeleteRequest
		return PermanentDeleteRequest(self.request_adapter, path_parameters)

	def snooze_reminder(self,
		user_id: str,
		calendarGroup_id: str,
		calendar_id: str,
		event_id: str,
		event_id1: str,
		event_id2: str,
	) -> SnoozeReminderRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if calendarGroup_id is None:
			raise TypeError("calendarGroup_id cannot be null.")
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")
		if event_id2 is None:
			raise TypeError("event_id2 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["calendarGroup%2Did"] =  calendarGroup_id
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1
		path_parameters["event%2Did2"] =  event_id2

		from .snooze_reminder import SnoozeReminderRequest
		return SnoozeReminderRequest(self.request_adapter, path_parameters)

	def tentatively_accept(self,
		user_id: str,
		calendarGroup_id: str,
		calendar_id: str,
		event_id: str,
		event_id1: str,
		event_id2: str,
	) -> TentativelyAcceptRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if calendarGroup_id is None:
			raise TypeError("calendarGroup_id cannot be null.")
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")
		if event_id2 is None:
			raise TypeError("event_id2 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["calendarGroup%2Did"] =  calendarGroup_id
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1
		path_parameters["event%2Did2"] =  event_id2

		from .tentatively_accept import TentativelyAcceptRequest
		return TentativelyAcceptRequest(self.request_adapter, path_parameters)

