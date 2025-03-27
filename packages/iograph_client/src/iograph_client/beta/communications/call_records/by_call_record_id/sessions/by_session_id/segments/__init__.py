# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_segment_id import BySegmentIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.call_records_segment_collection_response import CallRecordsSegmentCollectionResponse
from iograph_models.beta.call_records_segment import CallRecordsSegment
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class SegmentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/communications/callRecords/{callRecord%2Did}/sessions/{session%2Did}/segments", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CallRecordsSegmentCollectionResponse:
		"""
		Get segments from communications
		The list of segments involved in the session. Read-only. Nullable.
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
		return await self.request_adapter.send_async(request_info, CallRecordsSegmentCollectionResponse, error_mapping)

	async def post(
		self,
		body: CallRecordsSegment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CallRecordsSegment:
		"""
		Create new navigation property to segments for communications
		
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
		return await self.request_adapter.send_async(request_info, CallRecordsSegment, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> SegmentsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SegmentsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SegmentsRequest(self.request_adapter, self.path_parameters)

	def by_segment_id(self,
		callRecord_id: str,
		session_id: str,
		segment_id: str,
	) -> BySegmentIdRequest:
		if callRecord_id is None:
			raise TypeError("callRecord_id cannot be null.")
		if session_id is None:
			raise TypeError("session_id cannot be null.")
		if segment_id is None:
			raise TypeError("segment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["callRecord%2Did"] =  callRecord_id
		path_parameters["session%2Did"] =  session_id
		path_parameters["segment%2Did"] =  segment_id

		from .by_segment_id import BySegmentIdRequest
		return BySegmentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		callRecord_id: str,
		session_id: str,
	) -> CountRequest:
		if callRecord_id is None:
			raise TypeError("callRecord_id cannot be null.")
		if session_id is None:
			raise TypeError("session_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["callRecord%2Did"] =  callRecord_id
		path_parameters["session%2Did"] =  session_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

