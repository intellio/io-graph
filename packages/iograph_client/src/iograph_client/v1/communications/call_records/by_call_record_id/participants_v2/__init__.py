# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_participant_id import ByParticipantIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.call_records_participant_collection_response import CallRecordsParticipantCollectionResponse
from iograph_models.v1.call_records_participant import CallRecordsParticipant
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class Participants_v2Request(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/communications/callRecords/{callRecord%2Did}/participants_v2", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CallRecordsParticipantCollectionResponse:
		"""
		List participants_v2
		Get the list of participant objects associated with a callRecord.
		Find more info here: https://learn.microsoft.com/graph/api/callrecords-callrecord-list-participants_v2?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, CallRecordsParticipantCollectionResponse, error_mapping)

	async def post(
		self,
		body: CallRecordsParticipant,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CallRecordsParticipant:
		"""
		Create new navigation property to participants_v2 for communications
		
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
		return await self.request_adapter.send_async(request_info, CallRecordsParticipant, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> Participants_v2Request:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: Participants_v2Request
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return Participants_v2Request(self.request_adapter, self.path_parameters)

	def by_participant_id(self,
		callRecord_id: str,
		participant_id: str,
	) -> ByParticipantIdRequest:
		if callRecord_id is None:
			raise TypeError("callRecord_id cannot be null.")
		if participant_id is None:
			raise TypeError("participant_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["callRecord%2Did"] =  callRecord_id
		path_parameters["participant%2Did"] =  participant_id

		from .by_participant_id import ByParticipantIdRequest
		return ByParticipantIdRequest(self.request_adapter, path_parameters)

	def count(self,
		callRecord_id: str,
	) -> CountRequest:
		if callRecord_id is None:
			raise TypeError("callRecord_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["callRecord%2Did"] =  callRecord_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

