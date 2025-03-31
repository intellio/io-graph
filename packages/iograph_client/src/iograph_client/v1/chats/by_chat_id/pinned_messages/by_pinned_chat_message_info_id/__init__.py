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
	from .message import MessageRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.pinned_chat_message_info import PinnedChatMessageInfo
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByPinnedChatMessageInfoIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/chats/{chat%2Did}/pinnedMessages/{pinnedChatMessageInfo%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PinnedChatMessageInfo:
		"""
		Get pinnedMessages from chats
		A collection of all the pinned messages in the chat. Nullable.
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
		return await self.request_adapter.send_async(request_info, PinnedChatMessageInfo, error_mapping)

	async def patch(
		self,
		body: PinnedChatMessageInfo,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PinnedChatMessageInfo:
		"""
		Update the navigation property pinnedMessages in chats
		
		"""
		tags = ['chats.pinnedChatMessageInfo']

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
		return await self.request_adapter.send_async(request_info, PinnedChatMessageInfo, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Unpin a message from a chat
		Unpin a message from a chat.
		Find more info here: https://learn.microsoft.com/graph/api/chat-delete-pinnedmessages?view=graph-rest-1.0
		"""
		tags = ['chats.pinnedChatMessageInfo']
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



	def with_url(self, raw_url: str) -> ByPinnedChatMessageInfoIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPinnedChatMessageInfoIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPinnedChatMessageInfoIdRequest(self.request_adapter, self.path_parameters)

	def message(self,
		chat_id: str,
		pinnedChatMessageInfo_id: str,
	) -> MessageRequest:
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")
		if pinnedChatMessageInfo_id is None:
			raise TypeError("pinnedChatMessageInfo_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["chat%2Did"] =  chat_id
		path_parameters["pinnedChatMessageInfo%2Did"] =  pinnedChatMessageInfo_id

		from .message import MessageRequest
		return MessageRequest(self.request_adapter, path_parameters)

