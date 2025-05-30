# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .call_records_get_pstn_calls_with_fromdatetime_todatetime import CallRecordsGetPstnCallsWithFromDateTimeToDateTimeRequest
	from .call_records_get_direct_routing_calls_with_fromdatetime_todatetime import CallRecordsGetDirectRoutingCallsWithFromDateTimeToDateTimeRequest
	from .count import CountRequest
	from .by_call_record_id import ByCallRecordIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.call_records_call_record_collection_response import CallRecordsCallRecordCollectionResponse
from iograph_models.v1.call_records_call_record import CallRecordsCallRecord
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class CallRecordsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/communications/callRecords", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CallRecordsCallRecordCollectionResponse:
		"""
		List callRecords
		Get the list of callRecord objects and their properties. The results can be optionally filtered using the $filter query parameter on the startDateTime and participant id properties. Note that the listed call records don't include expandable relationships such as sessions and participants_v2. You can expand these relationships using Get callRecord for a specific record.
		Find more info here: https://learn.microsoft.com/graph/api/callrecords-cloudcommunications-list-callrecords?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, CallRecordsCallRecordCollectionResponse, error_mapping)

	async def post(
		self,
		body: CallRecordsCallRecord,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CallRecordsCallRecord:
		"""
		Create new navigation property to callRecords for communications
		
		"""
		tags = ['communications.callRecord']

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
		return await self.request_adapter.send_async(request_info, CallRecordsCallRecord, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> CallRecordsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CallRecordsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CallRecordsRequest(self.request_adapter, self.path_parameters)

	def by_call_record_id(self,
		callRecord_id: str,
	) -> ByCallRecordIdRequest:
		if callRecord_id is None:
			raise TypeError("callRecord_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["callRecord%2Did"] =  callRecord_id

		from .by_call_record_id import ByCallRecordIdRequest
		return ByCallRecordIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	def call_records_get_direct_routing_calls_with_fromdatetime_todatetime(self,
		fromDateTime: datetime,
		toDateTime: datetime,
	) -> CallRecordsGetDirectRoutingCallsWithFromDateTimeToDateTimeRequest:
		if fromDateTime is None:
			raise TypeError("fromDateTime cannot be null.")
		if toDateTime is None:
			raise TypeError("toDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fromDateTime"] =  fromDateTime
		path_parameters["toDateTime"] =  toDateTime

		from .call_records_get_direct_routing_calls_with_fromdatetime_todatetime import CallRecordsGetDirectRoutingCallsWithFromDateTimeToDateTimeRequest
		return CallRecordsGetDirectRoutingCallsWithFromDateTimeToDateTimeRequest(self.request_adapter, path_parameters)

	def call_records_get_pstn_calls_with_fromdatetime_todatetime(self,
		fromDateTime: datetime,
		toDateTime: datetime,
	) -> CallRecordsGetPstnCallsWithFromDateTimeToDateTimeRequest:
		if fromDateTime is None:
			raise TypeError("fromDateTime cannot be null.")
		if toDateTime is None:
			raise TypeError("toDateTime cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fromDateTime"] =  fromDateTime
		path_parameters["toDateTime"] =  toDateTime

		from .call_records_get_pstn_calls_with_fromdatetime_todatetime import CallRecordsGetPstnCallsWithFromDateTimeToDateTimeRequest
		return CallRecordsGetPstnCallsWithFromDateTimeToDateTimeRequest(self.request_adapter, path_parameters)

