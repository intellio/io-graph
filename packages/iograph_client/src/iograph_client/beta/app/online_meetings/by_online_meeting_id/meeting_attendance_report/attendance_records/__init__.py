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
	from .by_attendance_record_id import ByAttendanceRecordIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.attendance_record_collection_response import AttendanceRecordCollectionResponse
from iograph_models.beta.attendance_record import AttendanceRecord
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class AttendanceRecordsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/app/onlineMeetings/{onlineMeeting%2Did}/meetingAttendanceReport/attendanceRecords", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AttendanceRecordCollectionResponse:
		"""
		Get attendanceRecords from app
		List of attendance records of an attendance report. Read-only.
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
		return await self.request_adapter.send_async(request_info, AttendanceRecordCollectionResponse, error_mapping)

	async def post(
		self,
		body: AttendanceRecord,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AttendanceRecord:
		"""
		Create new navigation property to attendanceRecords for app
		
		"""
		tags = ['app.onlineMeeting']

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
		return await self.request_adapter.send_async(request_info, AttendanceRecord, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AttendanceRecordsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AttendanceRecordsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AttendanceRecordsRequest(self.request_adapter, self.path_parameters)

	def by_attendance_record_id(self,
		onlineMeeting_id: str,
		attendanceRecord_id: str,
	) -> ByAttendanceRecordIdRequest:
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")
		if attendanceRecord_id is None:
			raise TypeError("attendanceRecord_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id
		path_parameters["attendanceRecord%2Did"] =  attendanceRecord_id

		from .by_attendance_record_id import ByAttendanceRecordIdRequest
		return ByAttendanceRecordIdRequest(self.request_adapter, path_parameters)

	def count(self,
		onlineMeeting_id: str,
	) -> CountRequest:
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

