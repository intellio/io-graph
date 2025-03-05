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
	from .move import MoveRequest
	from .copy import CopyRequest
	from .messages import MessagesRequest
	from .message_rules import MessageRulesRequest
	from .child_folders import ChildFoldersRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.mail_folder import MailFolder


class ByMailFolderIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/mailFolders/{mailFolder%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MailFolder:
		"""
		Get mailFolders from users
		The user's mail folders. Read-only. Nullable.
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
		Update the navigation property mailFolders in users
		
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
		Delete navigation property mailFolders for users
		
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
		user_id: str,
		mailFolder_id: str,
	) -> ChildFoldersRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["mailFolder%2Did"] =  mailFolder_id

		from .child_folders import ChildFoldersRequest
		return ChildFoldersRequest(self.request_adapter, path_parameters)

	def message_rules(self,
		user_id: str,
		mailFolder_id: str,
	) -> MessageRulesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["mailFolder%2Did"] =  mailFolder_id

		from .message_rules import MessageRulesRequest
		return MessageRulesRequest(self.request_adapter, path_parameters)

	def messages(self,
		user_id: str,
		mailFolder_id: str,
	) -> MessagesRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["mailFolder%2Did"] =  mailFolder_id

		from .messages import MessagesRequest
		return MessagesRequest(self.request_adapter, path_parameters)

	def copy(self,
		user_id: str,
		mailFolder_id: str,
	) -> CopyRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["mailFolder%2Did"] =  mailFolder_id

		from .copy import CopyRequest
		return CopyRequest(self.request_adapter, path_parameters)

	def move(self,
		user_id: str,
		mailFolder_id: str,
	) -> MoveRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["mailFolder%2Did"] =  mailFolder_id

		from .move import MoveRequest
		return MoveRequest(self.request_adapter, path_parameters)

