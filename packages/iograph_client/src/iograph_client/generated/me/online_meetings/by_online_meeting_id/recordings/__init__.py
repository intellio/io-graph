# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_call_recording_id import ByCallRecordingIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.call_recording import CallRecording
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.call_recording_collection_response import CallRecordingCollectionResponse


class RecordingsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/me/onlineMeetings/{onlineMeeting%2Did}/recordings"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CallRecordingCollectionResponse:
		"""
		Get callRecording
		Get a callRecording object associated with a scheduled onlineMeeting. This API doesn't support getting call recordings from channel meetings. For a recording, this API returns the metadata of the single recording associated with the online meeting. For the content of a recording, this API returns the stream of bytes associated with the recording.
		Find more info here: https://learn.microsoft.com/graph/api/callrecording-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, CallRecordingCollectionResponse, error_mapping)

	async def post(
		self,
		body: CallRecording,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CallRecording:
		"""
		Create new navigation property to recordings for me
		
		"""
		tags = ['me.onlineMeeting']

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
		return await self.request_adapter.send_async(request_info, CallRecording, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_call_recording_id(self,
		onlineMeeting_id: str,
		callRecording_id: str,
	) -> ByCallRecordingIdRequest:
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")
		if callRecording_id is None:
			raise TypeError("callRecording_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id
		path_parameters["callRecording%2Did"] =  callRecording_id

		from .by_call_recording_id import ByCallRecordingIdRequest
		return ByCallRecordingIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

