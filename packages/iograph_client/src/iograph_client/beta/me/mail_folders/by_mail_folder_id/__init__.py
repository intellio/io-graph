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
	from .user_configurations import UserConfigurationsRequest
	from .operations import OperationsRequest
	from .update_all_messages_read_state import UpdateAllMessagesReadStateRequest
	from .permanent_delete import PermanentDeleteRequest
	from .move import MoveRequest
	from .copy import CopyRequest
	from .messages import MessagesRequest
	from .message_rules import MessageRulesRequest
	from .child_folders import ChildFoldersRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.mail_folder import MailFolder
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByMailFolderIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/mailFolders/{mailFolder%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MailFolder:
		"""
		Get mailFolder
		Retrieve the properties and relationships of a message folder object. The following list shows the two existing scenarios where an app can get another user's mail folder:
		Find more info here: https://learn.microsoft.com/graph/api/mailfolder-get?view=graph-rest-beta
		"""
		tags = ['me.mailFolder']

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
		Update mailSearchFolder
		Update the writable properties of a mailSearchFolder object.
		Find more info here: https://learn.microsoft.com/graph/api/mailsearchfolder-update?view=graph-rest-beta
		"""
		tags = ['me.mailFolder']

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
		Delete mailFolder
		Delete the specified mailFolder. The folder can be a mailSearchFolder. You can specify a mail folder by its folder ID, or by its well-known folder name, if one exists.
		Find more info here: https://learn.microsoft.com/graph/api/mailfolder-delete?view=graph-rest-beta
		"""
		tags = ['me.mailFolder']
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



	def with_url(self, raw_url: str) -> ByMailFolderIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByMailFolderIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByMailFolderIdRequest(self.request_adapter, self.path_parameters)

	def child_folders(self,
		mailFolder_id: str,
	) -> ChildFoldersRequest:
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailFolder%2Did"] =  mailFolder_id

		from .child_folders import ChildFoldersRequest
		return ChildFoldersRequest(self.request_adapter, path_parameters)

	def message_rules(self,
		mailFolder_id: str,
	) -> MessageRulesRequest:
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailFolder%2Did"] =  mailFolder_id

		from .message_rules import MessageRulesRequest
		return MessageRulesRequest(self.request_adapter, path_parameters)

	def messages(self,
		mailFolder_id: str,
	) -> MessagesRequest:
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailFolder%2Did"] =  mailFolder_id

		from .messages import MessagesRequest
		return MessagesRequest(self.request_adapter, path_parameters)

	def copy(self,
		mailFolder_id: str,
	) -> CopyRequest:
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailFolder%2Did"] =  mailFolder_id

		from .copy import CopyRequest
		return CopyRequest(self.request_adapter, path_parameters)

	def move(self,
		mailFolder_id: str,
	) -> MoveRequest:
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailFolder%2Did"] =  mailFolder_id

		from .move import MoveRequest
		return MoveRequest(self.request_adapter, path_parameters)

	def permanent_delete(self,
		mailFolder_id: str,
	) -> PermanentDeleteRequest:
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailFolder%2Did"] =  mailFolder_id

		from .permanent_delete import PermanentDeleteRequest
		return PermanentDeleteRequest(self.request_adapter, path_parameters)

	def update_all_messages_read_state(self,
		mailFolder_id: str,
	) -> UpdateAllMessagesReadStateRequest:
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailFolder%2Did"] =  mailFolder_id

		from .update_all_messages_read_state import UpdateAllMessagesReadStateRequest
		return UpdateAllMessagesReadStateRequest(self.request_adapter, path_parameters)

	def operations(self,
		mailFolder_id: str,
	) -> OperationsRequest:
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailFolder%2Did"] =  mailFolder_id

		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, path_parameters)

	def user_configurations(self,
		mailFolder_id: str,
	) -> UserConfigurationsRequest:
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailFolder%2Did"] =  mailFolder_id

		from .user_configurations import UserConfigurationsRequest
		return UserConfigurationsRequest(self.request_adapter, path_parameters)

