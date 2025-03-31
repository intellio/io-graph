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
	from .by_conversation_thread_id import ByConversationThreadIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.conversation_thread_collection_response import ConversationThreadCollectionResponse
from iograph_models.v1.conversation_thread import ConversationThread
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ThreadsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/conversations/{conversation%2Did}/threads", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ConversationThreadCollectionResponse:
		"""
		List threads
		Get all the threads in a group conversation. Note: You can also get all the threads of a group.
		Find more info here: https://learn.microsoft.com/graph/api/conversation-list-threads?view=graph-rest-1.0
		"""
		tags = ['groups.conversation']

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
		return await self.request_adapter.send_async(request_info, ConversationThreadCollectionResponse, error_mapping)

	async def post(
		self,
		body: ConversationThread,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ConversationThread:
		"""
		Create thread
		Create a new thread in the specified conversation.  A thread and post are created as specified. Use reply thread to further post 
to that thread. Or, if you get the post ID, you can also reply to that post in that thread. Note: You can also start a new conversation by first creating a thread.
		Find more info here: https://learn.microsoft.com/graph/api/conversation-post-threads?view=graph-rest-1.0
		"""
		tags = ['groups.conversation']

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
		return await self.request_adapter.send_async(request_info, ConversationThread, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ThreadsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ThreadsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ThreadsRequest(self.request_adapter, self.path_parameters)

	def by_conversation_thread_id(self,
		group_id: str,
		conversation_id: str,
		conversationThread_id: str,
	) -> ByConversationThreadIdRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if conversation_id is None:
			raise TypeError("conversation_id cannot be null.")
		if conversationThread_id is None:
			raise TypeError("conversationThread_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["conversation%2Did"] =  conversation_id
		path_parameters["conversationThread%2Did"] =  conversationThread_id

		from .by_conversation_thread_id import ByConversationThreadIdRequest
		return ByConversationThreadIdRequest(self.request_adapter, path_parameters)

	def count(self,
		group_id: str,
		conversation_id: str,
	) -> CountRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if conversation_id is None:
			raise TypeError("conversation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["conversation%2Did"] =  conversation_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

