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
	from .by_content_sharing_session_id import ByContentSharingSessionIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.content_sharing_session import ContentSharingSession
from iograph_models.beta.content_sharing_session_collection_response import ContentSharingSessionCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ContentSharingSessionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/communications/calls/{call%2Did}/contentSharingSessions", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ContentSharingSessionCollectionResponse:
		"""
		List contentSharingSessions
		Retrieve a list of contentSharingSession objects in a call.
		Find more info here: https://learn.microsoft.com/graph/api/call-list-contentsharingsessions?view=graph-rest-beta
		"""
		tags = ['communications.call']

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
		return await self.request_adapter.send_async(request_info, ContentSharingSessionCollectionResponse, error_mapping)

	async def post(
		self,
		body: ContentSharingSession,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ContentSharingSession:
		"""
		Create new navigation property to contentSharingSessions for communications
		
		"""
		tags = ['communications.call']

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
		return await self.request_adapter.send_async(request_info, ContentSharingSession, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ContentSharingSessionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ContentSharingSessionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ContentSharingSessionsRequest(self.request_adapter, self.path_parameters)

	def by_content_sharing_session_id(self,
		call_id: str,
		contentSharingSession_id: str,
	) -> ByContentSharingSessionIdRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")
		if contentSharingSession_id is None:
			raise TypeError("contentSharingSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id
		path_parameters["contentSharingSession%2Did"] =  contentSharingSession_id

		from .by_content_sharing_session_id import ByContentSharingSessionIdRequest
		return ByContentSharingSessionIdRequest(self.request_adapter, path_parameters)

	def count(self,
		call_id: str,
	) -> CountRequest:
		if call_id is None:
			raise TypeError("call_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["call%2Did"] =  call_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

