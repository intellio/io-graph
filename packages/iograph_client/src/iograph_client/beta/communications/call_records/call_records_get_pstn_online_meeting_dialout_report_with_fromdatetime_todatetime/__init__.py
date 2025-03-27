# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.call_records_get_pstn_online_meeting_dialout_report_with_fromdatetime_todatetime_get_response import Call_records_get_pstn_online_meeting_dialout_report_with_fromdatetime_todatetimeGetResponse


class CallRecordsGetPstnOnlineMeetingDialoutReportWithFromDateTimeToDateTimeRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/communications/callRecords/microsoft.graph.callRecords.getPstnOnlineMeetingDialoutReport(fromDateTime={fromDateTime},toDateTime={toDateTime})", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Call_records_get_pstn_online_meeting_dialout_report_with_fromdatetime_todatetimeGetResponse:
		"""
		Invoke function getPstnOnlineMeetingDialoutReport
		Get aggregated report of usage and money spent for the audio conferencing dial-out service over a selected period as a collection of pstnOnlineMeetingDialoutReport entries.
The report is aggregated by user, user location, destination context (domestic/international), and currency. The report includes:
		"""
		tags = ['communications.callRecord']

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
		return await self.request_adapter.send_async(request_info, Call_records_get_pstn_online_meeting_dialout_report_with_fromdatetime_todatetimeGetResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")

	def with_url(self, raw_url: str) -> CallRecordsGetPstnOnlineMeetingDialoutReportWithFromDateTimeToDateTimeRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CallRecordsGetPstnOnlineMeetingDialoutReportWithFromDateTimeToDateTimeRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CallRecordsGetPstnOnlineMeetingDialoutReportWithFromDateTimeToDateTimeRequest(self.request_adapter, self.path_parameters)

