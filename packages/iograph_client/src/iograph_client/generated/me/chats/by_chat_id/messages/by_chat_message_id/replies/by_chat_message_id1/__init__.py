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
	from .unset_reaction import UnsetReactionRequest
	from .undo_soft_delete import UndoSoftDeleteRequest
	from .soft_delete import SoftDeleteRequest
	from .set_reaction import SetReactionRequest
	from .hosted_contents import HostedContentsRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.chat_message import ChatMessage


class ByChatMessageId1Request(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/chats/{chat%2Did}/messages/{chatMessage%2Did}/replies/{chatMessage%2Did1}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ChatMessage:
		"""
		Get replies from me
		Replies for a specified message. Supports $expand for channel messages.
		"""
		tags = ['me.chat']

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
		return await self.request_adapter.send_async(request_info, ChatMessage, error_mapping)

	async def patch(
		self,
		body: ChatMessage,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ChatMessage:
		"""
		Update the navigation property replies in me
		
		"""
		tags = ['me.chat']

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
		return await self.request_adapter.send_async(request_info, ChatMessage, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property replies for me
		
		"""
		tags = ['me.chat']
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



	def with_url(self, raw_url: str) -> ByChatMessageId1Request:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByChatMessageId1Request
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByChatMessageId1Request(self.request_adapter, self.path_parameters)

	def hosted_contents(self,
		chat_id: str,
		chatMessage_id: str,
		chatMessage_id1: str,
	) -> HostedContentsRequest:
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")
		if chatMessage_id is None:
			raise TypeError("chatMessage_id cannot be null.")
		if chatMessage_id1 is None:
			raise TypeError("chatMessage_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["chat%2Did"] =  chat_id
		path_parameters["chatMessage%2Did"] =  chatMessage_id
		path_parameters["chatMessage%2Did1"] =  chatMessage_id1

		from .hosted_contents import HostedContentsRequest
		return HostedContentsRequest(self.request_adapter, path_parameters)

	def set_reaction(self,
		chat_id: str,
		chatMessage_id: str,
		chatMessage_id1: str,
	) -> SetReactionRequest:
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")
		if chatMessage_id is None:
			raise TypeError("chatMessage_id cannot be null.")
		if chatMessage_id1 is None:
			raise TypeError("chatMessage_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["chat%2Did"] =  chat_id
		path_parameters["chatMessage%2Did"] =  chatMessage_id
		path_parameters["chatMessage%2Did1"] =  chatMessage_id1

		from .set_reaction import SetReactionRequest
		return SetReactionRequest(self.request_adapter, path_parameters)

	def soft_delete(self,
		chat_id: str,
		chatMessage_id: str,
		chatMessage_id1: str,
	) -> SoftDeleteRequest:
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")
		if chatMessage_id is None:
			raise TypeError("chatMessage_id cannot be null.")
		if chatMessage_id1 is None:
			raise TypeError("chatMessage_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["chat%2Did"] =  chat_id
		path_parameters["chatMessage%2Did"] =  chatMessage_id
		path_parameters["chatMessage%2Did1"] =  chatMessage_id1

		from .soft_delete import SoftDeleteRequest
		return SoftDeleteRequest(self.request_adapter, path_parameters)

	def undo_soft_delete(self,
		chat_id: str,
		chatMessage_id: str,
		chatMessage_id1: str,
	) -> UndoSoftDeleteRequest:
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")
		if chatMessage_id is None:
			raise TypeError("chatMessage_id cannot be null.")
		if chatMessage_id1 is None:
			raise TypeError("chatMessage_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["chat%2Did"] =  chat_id
		path_parameters["chatMessage%2Did"] =  chatMessage_id
		path_parameters["chatMessage%2Did1"] =  chatMessage_id1

		from .undo_soft_delete import UndoSoftDeleteRequest
		return UndoSoftDeleteRequest(self.request_adapter, path_parameters)

	def unset_reaction(self,
		chat_id: str,
		chatMessage_id: str,
		chatMessage_id1: str,
	) -> UnsetReactionRequest:
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")
		if chatMessage_id is None:
			raise TypeError("chatMessage_id cannot be null.")
		if chatMessage_id1 is None:
			raise TypeError("chatMessage_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["chat%2Did"] =  chat_id
		path_parameters["chatMessage%2Did"] =  chatMessage_id
		path_parameters["chatMessage%2Did1"] =  chatMessage_id1

		from .unset_reaction import UnsetReactionRequest
		return UnsetReactionRequest(self.request_adapter, path_parameters)

