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
	from .get_all_retained_messages import GetAllRetainedMessagesRequest
	from .get_all_messages import GetAllMessagesRequest
	from .count import CountRequest
	from .by_chat_id import ByChatIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.chat import Chat
from iograph_models.models.chat_collection_response import ChatCollectionResponse


class ChatsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/chats", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ChatCollectionResponse:
		"""
		List chats
		Retrieve the list of chats that the user is part of. This method supports federation. When a user ID is provided, the calling application must belong to the same tenant that the user belongs to.
		Find more info here: https://learn.microsoft.com/graph/api/chat-list?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, ChatCollectionResponse, error_mapping)

	async def post(
		self,
		body: Chat,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Chat:
		"""
		Create new navigation property to chats for users
		
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
		return await self.request_adapter.send_async(request_info, Chat, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ChatsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ChatsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ChatsRequest(self.request_adapter, self.path_parameters)

	def by_chat_id(self,
		user_id: str,
		chat_id: str,
	) -> ByChatIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id

		from .by_chat_id import ByChatIdRequest
		return ByChatIdRequest(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def get_all_messages(self,
		user_id: str,
	) -> GetAllMessagesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .get_all_messages import GetAllMessagesRequest
		return GetAllMessagesRequest(self.request_adapter, path_parameters)

	def get_all_retained_messages(self,
		user_id: str,
	) -> GetAllRetainedMessagesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .get_all_retained_messages import GetAllRetainedMessagesRequest
		return GetAllRetainedMessagesRequest(self.request_adapter, path_parameters)

