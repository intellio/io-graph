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
	from .metadata_content import MetadataContentRequest
	from .content import ContentRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.call_transcript import CallTranscript


class ByCallTranscriptIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/onlineMeetings/{onlineMeeting%2Did}/transcripts/{callTranscript%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CallTranscript:
		"""
		Get callTranscript
		Retrieve a callTranscript object associated with a scheduled onlineMeeting. This API supports the retrieval of call transcripts from private chat meetings and channel meetings. Retrieving the transcript returns the metadata of the single transcript associated with the online meeting. Retrieving the content of the transcript returns the stream of text associated with the transcript.
		Find more info here: https://learn.microsoft.com/graph/api/calltranscript-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, CallTranscript, error_mapping)

	async def patch(
		self,
		body: CallTranscript,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CallTranscript:
		"""
		Update the navigation property transcripts in users
		
		"""
		tags = ['users.onlineMeeting']

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
		return await self.request_adapter.send_async(request_info, CallTranscript, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property transcripts for users
		
		"""
		tags = ['users.onlineMeeting']
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



	def with_url(self, raw_url: str) -> ByCallTranscriptIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByCallTranscriptIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByCallTranscriptIdRequest(self.request_adapter, self.path_parameters)

	def content(self,
		user_id: str,
		onlineMeeting_id: str,
		callTranscript_id: str,
	) -> ContentRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")
		if callTranscript_id is None:
			raise TypeError("callTranscript_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id
		path_parameters["callTranscript%2Did"] =  callTranscript_id

		from .content import ContentRequest
		return ContentRequest(self.request_adapter, path_parameters)

	def metadata_content(self,
		user_id: str,
		onlineMeeting_id: str,
		callTranscript_id: str,
	) -> MetadataContentRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")
		if callTranscript_id is None:
			raise TypeError("callTranscript_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id
		path_parameters["callTranscript%2Did"] =  callTranscript_id

		from .metadata_content import MetadataContentRequest
		return MetadataContentRequest(self.request_adapter, path_parameters)

