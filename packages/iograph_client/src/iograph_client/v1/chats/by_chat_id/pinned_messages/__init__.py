# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_pinned_chat_message_info_id import ByPinnedChatMessageInfoIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.pinned_chat_message_info_collection_response import PinnedChatMessageInfoCollectionResponse
from iograph_models.v1.pinned_chat_message_info import PinnedChatMessageInfo
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class PinnedMessagesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/chats/{chat%2Did}/pinnedMessages", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PinnedChatMessageInfoCollectionResponse:
		"""
		List pinnedChatMessages in a chat
		Get a list of pinnedChatMessages in a chat.
		Find more info here: https://learn.microsoft.com/graph/api/chat-list-pinnedmessages?view=graph-rest-1.0
		"""
		tags = ['chats.pinnedChatMessageInfo']

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
		return await self.request_adapter.send_async(request_info, PinnedChatMessageInfoCollectionResponse, error_mapping)

	async def post(
		self,
		body: PinnedChatMessageInfo,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PinnedChatMessageInfo:
		"""
		Pin a message in a chat
		Pin a chat message in the specified chat. This API cannot create a new chat; you must use the list chats method to retrieve the ID of an existing chat before you can pin a chat message.
		Find more info here: https://learn.microsoft.com/graph/api/chat-post-pinnedmessages?view=graph-rest-1.0
		"""
		tags = ['chats.pinnedChatMessageInfo']

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
		return await self.request_adapter.send_async(request_info, PinnedChatMessageInfo, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> PinnedMessagesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PinnedMessagesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PinnedMessagesRequest(self.request_adapter, self.path_parameters)

	def by_pinned_chat_message_info_id(self,
		chat_id: str,
		pinnedChatMessageInfo_id: str,
	) -> ByPinnedChatMessageInfoIdRequest:
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")
		if pinnedChatMessageInfo_id is None:
			raise TypeError("pinnedChatMessageInfo_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["chat%2Did"] =  chat_id
		path_parameters["pinnedChatMessageInfo%2Did"] =  pinnedChatMessageInfo_id

		from .by_pinned_chat_message_info_id import ByPinnedChatMessageInfoIdRequest
		return ByPinnedChatMessageInfoIdRequest(self.request_adapter, path_parameters)

	def count(self,
		chat_id: str,
	) -> CountRequest:
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["chat%2Did"] =  chat_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

