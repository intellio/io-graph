# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .transcripts import TranscriptsRequest
	from .recordings import RecordingsRequest
	from .send_virtual_appointment_sms import SendVirtualAppointmentSmsRequest
	from .send_virtual_appointment_reminder_sms import SendVirtualAppointmentReminderSmsRequest
	from .attendee_report import AttendeeReportRequest
	from .attendance_reports import AttendanceReportsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.online_meeting import OnlineMeeting


class ByOnlineMeetingIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/me/onlineMeetings/{onlineMeeting%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OnlineMeeting:
		"""
		Get onlineMeeting
		Retrieve the properties and relationships of an onlineMeeting object. For example, you can: Teams live event attendee report (deprecated) and Teams live event recordings (deprecated) are online meeting artifacts. For more information, see Online meeting artifacts and permissions.
		Find more info here: https://learn.microsoft.com/graph/api/onlinemeeting-get?view=graph-rest-1.0
		"""
		tags = ['me.onlineMeeting']

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
		return await self.request_adapter.send_async(request_info, OnlineMeeting, error_mapping)

	async def patch(
		self,
		body: OnlineMeeting,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OnlineMeeting:
		"""
		Update onlineMeeting
		Update the properties of the specified onlineMeeting object. For the list of properties that support updating, see the Request body section.
		Find more info here: https://learn.microsoft.com/graph/api/onlinemeeting-update?view=graph-rest-1.0
		"""
		tags = ['me.onlineMeeting']

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
		return await self.request_adapter.send_async(request_info, OnlineMeeting, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete onlineMeeting
		Delete an onlineMeeting object.
		Find more info here: https://learn.microsoft.com/graph/api/onlinemeeting-delete?view=graph-rest-1.0
		"""
		tags = ['me.onlineMeeting']
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
	def attendance_reports(self,
	) -> AttendanceReportsRequest:
		from .attendance_reports import AttendanceReportsRequest
		return AttendanceReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def attendee_report(self,
	) -> AttendeeReportRequest:
		from .attendee_report import AttendeeReportRequest
		return AttendeeReportRequest(self.request_adapter, self.path_parameters)

	@property
	def send_virtual_appointment_reminder_sms(self,
	) -> SendVirtualAppointmentReminderSmsRequest:
		from .send_virtual_appointment_reminder_sms import SendVirtualAppointmentReminderSmsRequest
		return SendVirtualAppointmentReminderSmsRequest(self.request_adapter, self.path_parameters)

	@property
	def send_virtual_appointment_sms(self,
	) -> SendVirtualAppointmentSmsRequest:
		from .send_virtual_appointment_sms import SendVirtualAppointmentSmsRequest
		return SendVirtualAppointmentSmsRequest(self.request_adapter, self.path_parameters)

	@property
	def recordings(self,
	) -> RecordingsRequest:
		from .recordings import RecordingsRequest
		return RecordingsRequest(self.request_adapter, self.path_parameters)

	@property
	def transcripts(self,
	) -> TranscriptsRequest:
		from .transcripts import TranscriptsRequest
		return TranscriptsRequest(self.request_adapter, self.path_parameters)

