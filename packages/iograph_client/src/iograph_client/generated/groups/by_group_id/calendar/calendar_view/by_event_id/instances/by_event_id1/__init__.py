# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
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
	from .extensions import ExtensionsRequest
	from .calendar import CalendarRequest
	from .attachments import AttachmentsRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.event import Event


class ByEventId1Request:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/groups/{group%2Did}/calendar/calendarView/{event%2Did}/instances/{event%2Did1}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Event:
		"""
		Get instances from groups
		The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions that have been modified, but does not include occurrences that have been cancelled from the series. Navigation property. Read-only. Nullable.
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

	@property
	def attachments(self,
	) -> AttachmentsRequest:
		from .attachments import AttachmentsRequest
		return AttachmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def calendar(self,
	) -> CalendarRequest:
		from .calendar import CalendarRequest
		return CalendarRequest(self.request_adapter, self.path_parameters)

	@property
	def extensions(self,
	) -> ExtensionsRequest:
		from .extensions import ExtensionsRequest
		return ExtensionsRequest(self.request_adapter, self.path_parameters)

	@property
	def accept(self,
	) -> AcceptRequest:
		from .accept import AcceptRequest
		return AcceptRequest(self.request_adapter, self.path_parameters)

	@property
	def cancel(self,
	) -> CancelRequest:
		from .cancel import CancelRequest
		return CancelRequest(self.request_adapter, self.path_parameters)

	@property
	def decline(self,
	) -> DeclineRequest:
		from .decline import DeclineRequest
		return DeclineRequest(self.request_adapter, self.path_parameters)

	@property
	def dismiss_reminder(self,
	) -> DismissReminderRequest:
		from .dismiss_reminder import DismissReminderRequest
		return DismissReminderRequest(self.request_adapter, self.path_parameters)

	@property
	def forward(self,
	) -> ForwardRequest:
		from .forward import ForwardRequest
		return ForwardRequest(self.request_adapter, self.path_parameters)

	@property
	def snooze_reminder(self,
	) -> SnoozeReminderRequest:
		from .snooze_reminder import SnoozeReminderRequest
		return SnoozeReminderRequest(self.request_adapter, self.path_parameters)

	@property
	def tentatively_accept(self,
	) -> TentativelyAcceptRequest:
		from .tentatively_accept import TentativelyAcceptRequest
		return TentativelyAcceptRequest(self.request_adapter, self.path_parameters)

