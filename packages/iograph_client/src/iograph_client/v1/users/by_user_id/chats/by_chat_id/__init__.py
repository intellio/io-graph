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
	from .tabs import TabsRequest
	from .pinned_messages import PinnedMessagesRequest
	from .permission_grants import PermissionGrantsRequest
	from .unhide_for_user import UnhideForUserRequest
	from .send_activity_notification import SendActivityNotificationRequest
	from .mark_chat_unread_for_user import MarkChatUnreadForUserRequest
	from .mark_chat_read_for_user import MarkChatReadForUserRequest
	from .hide_for_user import HideForUserRequest
	from .messages import MessagesRequest
	from .members import MembersRequest
	from .last_message_preview import LastMessagePreviewRequest
	from .installed_apps import InstalledAppsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.chat import Chat
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByChatIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/chats/{chat%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Chat:
		"""
		Get chat
		Retrieve a single chat (without its messages). This method supports federation. To access a chat, at least one chat member must belong to the tenant the request initiated from.
		Find more info here: https://learn.microsoft.com/graph/api/chat-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, Chat, error_mapping)

	async def patch(
		self,
		body: Chat,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Chat:
		"""
		Update the navigation property chats in users
		
		"""
		tags = ['users.chat']

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
		return await self.request_adapter.send_async(request_info, Chat, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property chats for users
		
		"""
		tags = ['users.chat']
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



	def with_url(self, raw_url: str) -> ByChatIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByChatIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByChatIdRequest(self.request_adapter, self.path_parameters)

	def installed_apps(self,
		user_id: str,
		chat_id: str,
	) -> InstalledAppsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id

		from .installed_apps import InstalledAppsRequest
		return InstalledAppsRequest(self.request_adapter, path_parameters)

	def last_message_preview(self,
		user_id: str,
		chat_id: str,
	) -> LastMessagePreviewRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id

		from .last_message_preview import LastMessagePreviewRequest
		return LastMessagePreviewRequest(self.request_adapter, path_parameters)

	def members(self,
		user_id: str,
		chat_id: str,
	) -> MembersRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id

		from .members import MembersRequest
		return MembersRequest(self.request_adapter, path_parameters)

	def messages(self,
		user_id: str,
		chat_id: str,
	) -> MessagesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id

		from .messages import MessagesRequest
		return MessagesRequest(self.request_adapter, path_parameters)

	def hide_for_user(self,
		user_id: str,
		chat_id: str,
	) -> HideForUserRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id

		from .hide_for_user import HideForUserRequest
		return HideForUserRequest(self.request_adapter, path_parameters)

	def mark_chat_read_for_user(self,
		user_id: str,
		chat_id: str,
	) -> MarkChatReadForUserRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id

		from .mark_chat_read_for_user import MarkChatReadForUserRequest
		return MarkChatReadForUserRequest(self.request_adapter, path_parameters)

	def mark_chat_unread_for_user(self,
		user_id: str,
		chat_id: str,
	) -> MarkChatUnreadForUserRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id

		from .mark_chat_unread_for_user import MarkChatUnreadForUserRequest
		return MarkChatUnreadForUserRequest(self.request_adapter, path_parameters)

	def send_activity_notification(self,
		user_id: str,
		chat_id: str,
	) -> SendActivityNotificationRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id

		from .send_activity_notification import SendActivityNotificationRequest
		return SendActivityNotificationRequest(self.request_adapter, path_parameters)

	def unhide_for_user(self,
		user_id: str,
		chat_id: str,
	) -> UnhideForUserRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id

		from .unhide_for_user import UnhideForUserRequest
		return UnhideForUserRequest(self.request_adapter, path_parameters)

	def permission_grants(self,
		user_id: str,
		chat_id: str,
	) -> PermissionGrantsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id

		from .permission_grants import PermissionGrantsRequest
		return PermissionGrantsRequest(self.request_adapter, path_parameters)

	def pinned_messages(self,
		user_id: str,
		chat_id: str,
	) -> PinnedMessagesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id

		from .pinned_messages import PinnedMessagesRequest
		return PinnedMessagesRequest(self.request_adapter, path_parameters)

	def tabs(self,
		user_id: str,
		chat_id: str,
	) -> TabsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if chat_id is None:
			raise TypeError("chat_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["chat%2Did"] =  chat_id

		from .tabs import TabsRequest
		return TabsRequest(self.request_adapter, path_parameters)

