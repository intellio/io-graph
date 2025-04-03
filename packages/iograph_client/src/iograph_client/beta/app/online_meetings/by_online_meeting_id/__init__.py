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
	from .transcripts import TranscriptsRequest
	from .registration import RegistrationRequest
	from .recordings import RecordingsRequest
	from .recording import RecordingRequest
	from .send_virtual_appointment_sms import SendVirtualAppointmentSmsRequest
	from .send_virtual_appointment_reminder_sms import SendVirtualAppointmentReminderSmsRequest
	from .get_virtual_appointment_join_web_url import GetVirtualAppointmentJoinWebUrlRequest
	from .meeting_attendance_report import MeetingAttendanceReportRequest
	from .broadcast_recording import BroadcastRecordingRequest
	from .attendee_report import AttendeeReportRequest
	from .attendance_reports import AttendanceReportsRequest
	from .alternative_recording import AlternativeRecordingRequest
	from .ai_insights import AiInsightsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.online_meeting import OnlineMeeting


class ByOnlineMeetingIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/app/onlineMeetings/{onlineMeeting%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OnlineMeeting:
		"""
		Get onlineMeetings from app
		
		"""
		tags = ['app.onlineMeeting']

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
		Update the navigation property onlineMeetings in app
		
		"""
		tags = ['app.onlineMeeting']

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
		Delete navigation property onlineMeetings for app
		
		"""
		tags = ['app.onlineMeeting']
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



	def with_url(self, raw_url: str) -> ByOnlineMeetingIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByOnlineMeetingIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByOnlineMeetingIdRequest(self.request_adapter, self.path_parameters)

	def ai_insights(self,
		onlineMeeting_id: str,
	) -> AiInsightsRequest:
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id

		from .ai_insights import AiInsightsRequest
		return AiInsightsRequest(self.request_adapter, path_parameters)

	def alternative_recording(self,
		onlineMeeting_id: str,
	) -> AlternativeRecordingRequest:
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id

		from .alternative_recording import AlternativeRecordingRequest
		return AlternativeRecordingRequest(self.request_adapter, path_parameters)

	def attendance_reports(self,
		onlineMeeting_id: str,
	) -> AttendanceReportsRequest:
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id

		from .attendance_reports import AttendanceReportsRequest
		return AttendanceReportsRequest(self.request_adapter, path_parameters)

	def attendee_report(self,
		onlineMeeting_id: str,
	) -> AttendeeReportRequest:
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id

		from .attendee_report import AttendeeReportRequest
		return AttendeeReportRequest(self.request_adapter, path_parameters)

	def broadcast_recording(self,
		onlineMeeting_id: str,
	) -> BroadcastRecordingRequest:
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id

		from .broadcast_recording import BroadcastRecordingRequest
		return BroadcastRecordingRequest(self.request_adapter, path_parameters)

	def meeting_attendance_report(self,
		onlineMeeting_id: str,
	) -> MeetingAttendanceReportRequest:
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id

		from .meeting_attendance_report import MeetingAttendanceReportRequest
		return MeetingAttendanceReportRequest(self.request_adapter, path_parameters)

	def get_virtual_appointment_join_web_url(self,
		onlineMeeting_id: str,
	) -> GetVirtualAppointmentJoinWebUrlRequest:
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id

		from .get_virtual_appointment_join_web_url import GetVirtualAppointmentJoinWebUrlRequest
		return GetVirtualAppointmentJoinWebUrlRequest(self.request_adapter, path_parameters)

	def send_virtual_appointment_reminder_sms(self,
		onlineMeeting_id: str,
	) -> SendVirtualAppointmentReminderSmsRequest:
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id

		from .send_virtual_appointment_reminder_sms import SendVirtualAppointmentReminderSmsRequest
		return SendVirtualAppointmentReminderSmsRequest(self.request_adapter, path_parameters)

	def send_virtual_appointment_sms(self,
		onlineMeeting_id: str,
	) -> SendVirtualAppointmentSmsRequest:
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id

		from .send_virtual_appointment_sms import SendVirtualAppointmentSmsRequest
		return SendVirtualAppointmentSmsRequest(self.request_adapter, path_parameters)

	def recording(self,
		onlineMeeting_id: str,
	) -> RecordingRequest:
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id

		from .recording import RecordingRequest
		return RecordingRequest(self.request_adapter, path_parameters)

	def recordings(self,
		onlineMeeting_id: str,
	) -> RecordingsRequest:
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id

		from .recordings import RecordingsRequest
		return RecordingsRequest(self.request_adapter, path_parameters)

	def registration(self,
		onlineMeeting_id: str,
	) -> RegistrationRequest:
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id

		from .registration import RegistrationRequest
		return RegistrationRequest(self.request_adapter, path_parameters)

	def transcripts(self,
		onlineMeeting_id: str,
	) -> TranscriptsRequest:
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id

		from .transcripts import TranscriptsRequest
		return TranscriptsRequest(self.request_adapter, path_parameters)

