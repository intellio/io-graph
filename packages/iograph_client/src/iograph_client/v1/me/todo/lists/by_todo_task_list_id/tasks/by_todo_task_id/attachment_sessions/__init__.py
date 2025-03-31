# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_attachment_session_id import ByAttachmentSessionIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.v1.attachment_session_collection_response import AttachmentSessionCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class AttachmentSessionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/todo/lists/{todoTaskList%2Did}/tasks/{todoTask%2Did}/attachmentSessions", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AttachmentSessionCollectionResponse:
		"""
		Get attachmentSessions from me
		
		"""
		tags = ['me.todo']

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
		return await self.request_adapter.send_async(request_info, AttachmentSessionCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> AttachmentSessionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AttachmentSessionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AttachmentSessionsRequest(self.request_adapter, self.path_parameters)

	def by_attachment_session_id(self,
		todoTaskList_id: str,
		todoTask_id: str,
		attachmentSession_id: str,
	) -> ByAttachmentSessionIdRequest:
		if todoTaskList_id is None:
			raise TypeError("todoTaskList_id cannot be null.")
		if todoTask_id is None:
			raise TypeError("todoTask_id cannot be null.")
		if attachmentSession_id is None:
			raise TypeError("attachmentSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["todoTaskList%2Did"] =  todoTaskList_id
		path_parameters["todoTask%2Did"] =  todoTask_id
		path_parameters["attachmentSession%2Did"] =  attachmentSession_id

		from .by_attachment_session_id import ByAttachmentSessionIdRequest
		return ByAttachmentSessionIdRequest(self.request_adapter, path_parameters)

	def count(self,
		todoTaskList_id: str,
		todoTask_id: str,
	) -> CountRequest:
		if todoTaskList_id is None:
			raise TypeError("todoTaskList_id cannot be null.")
		if todoTask_id is None:
			raise TypeError("todoTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["todoTaskList%2Did"] =  todoTaskList_id
		path_parameters["todoTask%2Did"] =  todoTask_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

