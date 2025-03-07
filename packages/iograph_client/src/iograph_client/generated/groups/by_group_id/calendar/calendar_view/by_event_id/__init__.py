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
	from .tentatively_accept import TentativelyAcceptRequest
	from .snooze_reminder import SnoozeReminderRequest
	from .forward import ForwardRequest
	from .dismiss_reminder import DismissReminderRequest
	from .decline import DeclineRequest
	from .cancel import CancelRequest
	from .accept import AcceptRequest
	from .instances import InstancesRequest
	from .extensions import ExtensionsRequest
	from .calendar import CalendarRequest
	from .attachments import AttachmentsRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.event import Event
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByEventIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/calendar/calendarView/{event%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Event:
		"""
		Get calendarView from groups
		The calendar view for the calendar. Navigation property. Read-only.
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
		return await self.request_adapter.send_async(request_info, Event, error_mapping)

	class GetQueryParams(BaseModel):
		startDateTime: str = Field(default=None,serialization_alias="startDateTime")
		endDateTime: str = Field(default=None,serialization_alias="endDateTime")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ByEventIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByEventIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByEventIdRequest(self.request_adapter, self.path_parameters)

	def attachments(self,
		group_id: str,
		event_id: str,
	) -> AttachmentsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["event%2Did"] =  event_id

		from .attachments import AttachmentsRequest
		return AttachmentsRequest(self.request_adapter, path_parameters)

	def calendar(self,
		group_id: str,
		event_id: str,
	) -> CalendarRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["event%2Did"] =  event_id

		from .calendar import CalendarRequest
		return CalendarRequest(self.request_adapter, path_parameters)

	def extensions(self,
		group_id: str,
		event_id: str,
	) -> ExtensionsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["event%2Did"] =  event_id

		from .extensions import ExtensionsRequest
		return ExtensionsRequest(self.request_adapter, path_parameters)

	def instances(self,
		group_id: str,
		event_id: str,
	) -> InstancesRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["event%2Did"] =  event_id

		from .instances import InstancesRequest
		return InstancesRequest(self.request_adapter, path_parameters)

	def accept(self,
		group_id: str,
		event_id: str,
	) -> AcceptRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["event%2Did"] =  event_id

		from .accept import AcceptRequest
		return AcceptRequest(self.request_adapter, path_parameters)

	def cancel(self,
		group_id: str,
		event_id: str,
	) -> CancelRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["event%2Did"] =  event_id

		from .cancel import CancelRequest
		return CancelRequest(self.request_adapter, path_parameters)

	def decline(self,
		group_id: str,
		event_id: str,
	) -> DeclineRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["event%2Did"] =  event_id

		from .decline import DeclineRequest
		return DeclineRequest(self.request_adapter, path_parameters)

	def dismiss_reminder(self,
		group_id: str,
		event_id: str,
	) -> DismissReminderRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["event%2Did"] =  event_id

		from .dismiss_reminder import DismissReminderRequest
		return DismissReminderRequest(self.request_adapter, path_parameters)

	def forward(self,
		group_id: str,
		event_id: str,
	) -> ForwardRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["event%2Did"] =  event_id

		from .forward import ForwardRequest
		return ForwardRequest(self.request_adapter, path_parameters)

	def snooze_reminder(self,
		group_id: str,
		event_id: str,
	) -> SnoozeReminderRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["event%2Did"] =  event_id

		from .snooze_reminder import SnoozeReminderRequest
		return SnoozeReminderRequest(self.request_adapter, path_parameters)

	def tentatively_accept(self,
		group_id: str,
		event_id: str,
	) -> TentativelyAcceptRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["event%2Did"] =  event_id

		from .tentatively_accept import TentativelyAcceptRequest
		return TentativelyAcceptRequest(self.request_adapter, path_parameters)

