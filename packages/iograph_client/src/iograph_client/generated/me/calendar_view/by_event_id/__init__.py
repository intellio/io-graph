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
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.event import Event


class ByEventIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/calendarView/{event%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Event:
		"""
		Get calendarView from me
		The calendar view for the calendar. Read-only. Nullable.
		"""
		tags = ['me.event']

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
		event_id: str,
	) -> AttachmentsRequest:
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["event%2Did"] =  event_id

		from .attachments import AttachmentsRequest
		return AttachmentsRequest(self.request_adapter, path_parameters)

	def calendar(self,
		event_id: str,
	) -> CalendarRequest:
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["event%2Did"] =  event_id

		from .calendar import CalendarRequest
		return CalendarRequest(self.request_adapter, path_parameters)

	def extensions(self,
		event_id: str,
	) -> ExtensionsRequest:
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["event%2Did"] =  event_id

		from .extensions import ExtensionsRequest
		return ExtensionsRequest(self.request_adapter, path_parameters)

	def instances(self,
		event_id: str,
	) -> InstancesRequest:
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["event%2Did"] =  event_id

		from .instances import InstancesRequest
		return InstancesRequest(self.request_adapter, path_parameters)

	def accept(self,
		event_id: str,
	) -> AcceptRequest:
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["event%2Did"] =  event_id

		from .accept import AcceptRequest
		return AcceptRequest(self.request_adapter, path_parameters)

	def cancel(self,
		event_id: str,
	) -> CancelRequest:
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["event%2Did"] =  event_id

		from .cancel import CancelRequest
		return CancelRequest(self.request_adapter, path_parameters)

	def decline(self,
		event_id: str,
	) -> DeclineRequest:
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["event%2Did"] =  event_id

		from .decline import DeclineRequest
		return DeclineRequest(self.request_adapter, path_parameters)

	def dismiss_reminder(self,
		event_id: str,
	) -> DismissReminderRequest:
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["event%2Did"] =  event_id

		from .dismiss_reminder import DismissReminderRequest
		return DismissReminderRequest(self.request_adapter, path_parameters)

	def forward(self,
		event_id: str,
	) -> ForwardRequest:
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["event%2Did"] =  event_id

		from .forward import ForwardRequest
		return ForwardRequest(self.request_adapter, path_parameters)

	def snooze_reminder(self,
		event_id: str,
	) -> SnoozeReminderRequest:
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["event%2Did"] =  event_id

		from .snooze_reminder import SnoozeReminderRequest
		return SnoozeReminderRequest(self.request_adapter, path_parameters)

	def tentatively_accept(self,
		event_id: str,
	) -> TentativelyAcceptRequest:
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["event%2Did"] =  event_id

		from .tentatively_accept import TentativelyAcceptRequest
		return TentativelyAcceptRequest(self.request_adapter, path_parameters)

