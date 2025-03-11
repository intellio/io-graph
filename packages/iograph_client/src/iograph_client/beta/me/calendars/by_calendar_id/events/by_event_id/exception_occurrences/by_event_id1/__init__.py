# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
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
	from .instances import InstancesRequest
	from .extensions import ExtensionsRequest
	from .calendar import CalendarRequest
	from .attachments import AttachmentsRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.event import Event


class ByEventId1Request(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/calendars/{calendar%2Did}/events/{event%2Did}/exceptionOccurrences/{event%2Did1}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Event:
		"""
		Get exceptionOccurrences from me
		
		"""
		tags = ['me.calendar']

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

	def with_url(self, raw_url: str) -> ByEventId1Request:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByEventId1Request
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByEventId1Request(self.request_adapter, self.path_parameters)

	def attachments(self,
		calendar_id: str,
		event_id: str,
		event_id1: str,
	) -> AttachmentsRequest:
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1

		from .attachments import AttachmentsRequest
		return AttachmentsRequest(self.request_adapter, path_parameters)

	def calendar(self,
		calendar_id: str,
		event_id: str,
		event_id1: str,
	) -> CalendarRequest:
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1

		from .calendar import CalendarRequest
		return CalendarRequest(self.request_adapter, path_parameters)

	def extensions(self,
		calendar_id: str,
		event_id: str,
		event_id1: str,
	) -> ExtensionsRequest:
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1

		from .extensions import ExtensionsRequest
		return ExtensionsRequest(self.request_adapter, path_parameters)

	def instances(self,
		calendar_id: str,
		event_id: str,
		event_id1: str,
	) -> InstancesRequest:
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1

		from .instances import InstancesRequest
		return InstancesRequest(self.request_adapter, path_parameters)

	def accept(self,
		calendar_id: str,
		event_id: str,
		event_id1: str,
	) -> AcceptRequest:
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1

		from .accept import AcceptRequest
		return AcceptRequest(self.request_adapter, path_parameters)

	def cancel(self,
		calendar_id: str,
		event_id: str,
		event_id1: str,
	) -> CancelRequest:
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1

		from .cancel import CancelRequest
		return CancelRequest(self.request_adapter, path_parameters)

	def decline(self,
		calendar_id: str,
		event_id: str,
		event_id1: str,
	) -> DeclineRequest:
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1

		from .decline import DeclineRequest
		return DeclineRequest(self.request_adapter, path_parameters)

	def dismiss_reminder(self,
		calendar_id: str,
		event_id: str,
		event_id1: str,
	) -> DismissReminderRequest:
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1

		from .dismiss_reminder import DismissReminderRequest
		return DismissReminderRequest(self.request_adapter, path_parameters)

	def forward(self,
		calendar_id: str,
		event_id: str,
		event_id1: str,
	) -> ForwardRequest:
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1

		from .forward import ForwardRequest
		return ForwardRequest(self.request_adapter, path_parameters)

	def permanent_delete(self,
		calendar_id: str,
		event_id: str,
		event_id1: str,
	) -> PermanentDeleteRequest:
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1

		from .permanent_delete import PermanentDeleteRequest
		return PermanentDeleteRequest(self.request_adapter, path_parameters)

	def snooze_reminder(self,
		calendar_id: str,
		event_id: str,
		event_id1: str,
	) -> SnoozeReminderRequest:
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1

		from .snooze_reminder import SnoozeReminderRequest
		return SnoozeReminderRequest(self.request_adapter, path_parameters)

	def tentatively_accept(self,
		calendar_id: str,
		event_id: str,
		event_id1: str,
	) -> TentativelyAcceptRequest:
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1

		from .tentatively_accept import TentativelyAcceptRequest
		return TentativelyAcceptRequest(self.request_adapter, path_parameters)

