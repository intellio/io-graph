# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .user_configurations import UserConfigurationsRequest
	from .operations import OperationsRequest
	from .update_all_messages_read_state import UpdateAllMessagesReadStateRequest
	from .permanent_delete import PermanentDeleteRequest
	from .move import MoveRequest
	from .copy import CopyRequest
	from .messages import MessagesRequest
	from .message_rules import MessageRulesRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.mail_folder import MailFolder
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByMailFolderId1Request(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/mailFolders/{mailFolder%2Did}/childFolders/{mailFolder%2Did1}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MailFolder:
		"""
		Get childFolders from users
		The collection of child folders in the mailFolder.
		"""
		tags = ['users.mailFolder']

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
		return await self.request_adapter.send_async(request_info, MailFolder, error_mapping)

	async def patch(
		self,
		body: MailFolder,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MailFolder:
		"""
		Update the navigation property childFolders in users
		
		"""
		tags = ['users.mailFolder']

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
		return await self.request_adapter.send_async(request_info, MailFolder, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property childFolders for users
		
		"""
		tags = ['users.mailFolder']
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
		includeHiddenFolders: str = Field(default=None,serialization_alias="includeHiddenFolders")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> ByMailFolderId1Request:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByMailFolderId1Request
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByMailFolderId1Request(self.request_adapter, self.path_parameters)

	def message_rules(self,
		user_id: str,
		mailFolder_id: str,
		mailFolder_id1: str,
	) -> MessageRulesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")
		if mailFolder_id1 is None:
			raise TypeError("mailFolder_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["mailFolder%2Did"] =  mailFolder_id
		path_parameters["mailFolder%2Did1"] =  mailFolder_id1

		from .message_rules import MessageRulesRequest
		return MessageRulesRequest(self.request_adapter, path_parameters)

	def messages(self,
		user_id: str,
		mailFolder_id: str,
		mailFolder_id1: str,
	) -> MessagesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")
		if mailFolder_id1 is None:
			raise TypeError("mailFolder_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["mailFolder%2Did"] =  mailFolder_id
		path_parameters["mailFolder%2Did1"] =  mailFolder_id1

		from .messages import MessagesRequest
		return MessagesRequest(self.request_adapter, path_parameters)

	def copy(self,
		user_id: str,
		mailFolder_id: str,
		mailFolder_id1: str,
	) -> CopyRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")
		if mailFolder_id1 is None:
			raise TypeError("mailFolder_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["mailFolder%2Did"] =  mailFolder_id
		path_parameters["mailFolder%2Did1"] =  mailFolder_id1

		from .copy import CopyRequest
		return CopyRequest(self.request_adapter, path_parameters)

	def move(self,
		user_id: str,
		mailFolder_id: str,
		mailFolder_id1: str,
	) -> MoveRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")
		if mailFolder_id1 is None:
			raise TypeError("mailFolder_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["mailFolder%2Did"] =  mailFolder_id
		path_parameters["mailFolder%2Did1"] =  mailFolder_id1

		from .move import MoveRequest
		return MoveRequest(self.request_adapter, path_parameters)

	def permanent_delete(self,
		user_id: str,
		mailFolder_id: str,
		mailFolder_id1: str,
	) -> PermanentDeleteRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")
		if mailFolder_id1 is None:
			raise TypeError("mailFolder_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["mailFolder%2Did"] =  mailFolder_id
		path_parameters["mailFolder%2Did1"] =  mailFolder_id1

		from .permanent_delete import PermanentDeleteRequest
		return PermanentDeleteRequest(self.request_adapter, path_parameters)

	def update_all_messages_read_state(self,
		user_id: str,
		mailFolder_id: str,
		mailFolder_id1: str,
	) -> UpdateAllMessagesReadStateRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")
		if mailFolder_id1 is None:
			raise TypeError("mailFolder_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["mailFolder%2Did"] =  mailFolder_id
		path_parameters["mailFolder%2Did1"] =  mailFolder_id1

		from .update_all_messages_read_state import UpdateAllMessagesReadStateRequest
		return UpdateAllMessagesReadStateRequest(self.request_adapter, path_parameters)

	def operations(self,
		user_id: str,
		mailFolder_id: str,
		mailFolder_id1: str,
	) -> OperationsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")
		if mailFolder_id1 is None:
			raise TypeError("mailFolder_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["mailFolder%2Did"] =  mailFolder_id
		path_parameters["mailFolder%2Did1"] =  mailFolder_id1

		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, path_parameters)

	def user_configurations(self,
		user_id: str,
		mailFolder_id: str,
		mailFolder_id1: str,
	) -> UserConfigurationsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")
		if mailFolder_id1 is None:
			raise TypeError("mailFolder_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["mailFolder%2Did"] =  mailFolder_id
		path_parameters["mailFolder%2Did1"] =  mailFolder_id1

		from .user_configurations import UserConfigurationsRequest
		return UserConfigurationsRequest(self.request_adapter, path_parameters)

