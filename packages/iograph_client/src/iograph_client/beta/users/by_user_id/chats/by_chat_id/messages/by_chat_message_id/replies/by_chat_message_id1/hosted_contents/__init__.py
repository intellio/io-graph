# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_chat_message_hosted_content_id import ByChatMessageHostedContentIdRequest
	from ...........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.chat_message_hosted_content import ChatMessageHostedContent
from iograph_models.beta.chat_message_hosted_content_collection_response import ChatMessageHostedContentCollectionResponse


class HostedContentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/chats/{chat%2Did}/messages/{chatMessage%2Did}/replies/{chatMessage%2Did1}/hostedContents", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ChatMessageHostedContentCollectionResponse:
		"""
		Get hostedContents from users
		Content in a message hosted by Microsoft Teams - for example, images or code snippets.
		"""
		tags = ['users.chat']

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
		return await self.request_adapter.send_async(request_info, ChatMessageHostedContentCollectionResponse, error_mapping)

	async def post(
		self,
		body: ChatMessageHostedContent,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ChatMessageHostedContent:
		"""
		Create new navigation property to hostedContents for users
		
		"""
		tags = ['users.chat']

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
		return await self.request_adapter.send_async(request_info, ChatMessageHostedContent, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> HostedContentsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: HostedContentsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return HostedContentsRequest(self.request_adapter, self.path_parameters)

	def by_chat_message_hosted_content_id(self,
		user_id: str,
		chat_id: str,
		chatMessage_id: str,
		chatMessage_id1: str,
		chatMessageHostedContent_id: str,
	) -> ByChatMessageHostedContentIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")
		if chatMessage_id is None:
			raise TypeError("chatMessage_id cannot be null.")
		if chatMessage_id1 is None:
			raise TypeError("chatMessage_id1 cannot be null.")
		if chatMessageHostedContent_id is None:
			raise TypeError("chatMessageHostedContent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id
		path_parameters["chatMessage%2Did"] =  chatMessage_id
		path_parameters["chatMessage%2Did1"] =  chatMessage_id1
		path_parameters["chatMessageHostedContent%2Did"] =  chatMessageHostedContent_id

		from .by_chat_message_hosted_content_id import ByChatMessageHostedContentIdRequest
		return ByChatMessageHostedContentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
		chat_id: str,
		chatMessage_id: str,
		chatMessage_id1: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")
		if chatMessage_id is None:
			raise TypeError("chatMessage_id cannot be null.")
		if chatMessage_id1 is None:
			raise TypeError("chatMessage_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id
		path_parameters["chatMessage%2Did"] =  chatMessage_id
		path_parameters["chatMessage%2Did1"] =  chatMessage_id1

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

