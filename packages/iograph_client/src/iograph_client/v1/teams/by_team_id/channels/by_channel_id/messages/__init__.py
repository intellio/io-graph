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
	from .delta import DeltaRequest
	from .count import CountRequest
	from .by_chat_message_id import ByChatMessageIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.chat_message_collection_response import ChatMessageCollectionResponse
from iograph_models.v1.chat_message import ChatMessage
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class MessagesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/teams/{team%2Did}/channels/{channel%2Did}/messages", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ChatMessageCollectionResponse:
		"""
		List channel messages
		Retrieve the list of messages (without the replies) in a channel of a team.  To get the replies for a message, call the list message replies or the get message reply API.  This method supports federation. To list channel messages in application context, the request must be made from the tenant that the channel owner belongs to (represented by the tenantId property on the channel).
		Find more info here: https://learn.microsoft.com/graph/api/channel-list-messages?view=graph-rest-1.0
		"""
		tags = ['teams.channel']

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
		return await self.request_adapter.send_async(request_info, ChatMessageCollectionResponse, error_mapping)

	async def post(
		self,
		body: ChatMessage,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ChatMessage:
		"""
		Send chatMessage in channel
		Send a new chatMessage in the specified channel.
		Find more info here: https://learn.microsoft.com/graph/api/channel-post-messages?view=graph-rest-1.0
		"""
		tags = ['teams.channel']

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
		return await self.request_adapter.send_async(request_info, ChatMessage, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> MessagesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MessagesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MessagesRequest(self.request_adapter, self.path_parameters)

	def by_chat_message_id(self,
		team_id: str,
		channel_id: str,
		chatMessage_id: str,
	) -> ByChatMessageIdRequest:
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")
		if chatMessage_id is None:
			raise TypeError("chatMessage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["team%2Did"] =  team_id
		path_parameters["channel%2Did"] =  channel_id
		path_parameters["chatMessage%2Did"] =  chatMessage_id

		from .by_chat_message_id import ByChatMessageIdRequest
		return ByChatMessageIdRequest(self.request_adapter, path_parameters)

	def count(self,
		team_id: str,
		channel_id: str,
	) -> CountRequest:
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["team%2Did"] =  team_id
		path_parameters["channel%2Did"] =  channel_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def delta(self,
		team_id: str,
		channel_id: str,
	) -> DeltaRequest:
		if team_id is None:
			raise TypeError("team_id cannot be null.")
		if channel_id is None:
			raise TypeError("channel_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["team%2Did"] =  team_id
		path_parameters["channel%2Did"] =  channel_id

		from .delta import DeltaRequest
		return DeltaRequest(self.request_adapter, path_parameters)

