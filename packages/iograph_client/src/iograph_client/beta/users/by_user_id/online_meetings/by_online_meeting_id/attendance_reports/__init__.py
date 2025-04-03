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
	from .count import CountRequest
	from .by_meeting_attendance_report_id import ByMeetingAttendanceReportIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.meeting_attendance_report_collection_response import MeetingAttendanceReportCollectionResponse
from iograph_models.beta.meeting_attendance_report import MeetingAttendanceReport


class AttendanceReportsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/onlineMeetings/{onlineMeeting%2Did}/attendanceReports", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MeetingAttendanceReportCollectionResponse:
		"""
		Get attendanceReports from users
		The attendance reports of an online meeting. Read-only.
		"""
		tags = ['users.onlineMeeting']

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
		return await self.request_adapter.send_async(request_info, MeetingAttendanceReportCollectionResponse, error_mapping)

	async def post(
		self,
		body: MeetingAttendanceReport,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MeetingAttendanceReport:
		"""
		Create new navigation property to attendanceReports for users
		
		"""
		tags = ['users.onlineMeeting']

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
		return await self.request_adapter.send_async(request_info, MeetingAttendanceReport, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AttendanceReportsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AttendanceReportsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AttendanceReportsRequest(self.request_adapter, self.path_parameters)

	def by_meeting_attendance_report_id(self,
		user_id: str,
		onlineMeeting_id: str,
		meetingAttendanceReport_id: str,
	) -> ByMeetingAttendanceReportIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")
		if meetingAttendanceReport_id is None:
			raise TypeError("meetingAttendanceReport_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id
		path_parameters["meetingAttendanceReport%2Did"] =  meetingAttendanceReport_id

		from .by_meeting_attendance_report_id import ByMeetingAttendanceReportIdRequest
		return ByMeetingAttendanceReportIdRequest(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
		onlineMeeting_id: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

