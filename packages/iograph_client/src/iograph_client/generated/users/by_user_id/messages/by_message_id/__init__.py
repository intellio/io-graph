# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .send import SendRequest
	from .reply_all import ReplyAllRequest
	from .reply import ReplyRequest
	from .move import MoveRequest
	from .forward import ForwardRequest
	from .create_reply_all import CreateReplyAllRequest
	from .create_reply import CreateReplyRequest
	from .create_forward import CreateForwardRequest
	from .copy import CopyRequest
	from .extensions import ExtensionsRequest
	from .attachments import AttachmentsRequest
	from .value import ValueRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.message import Message
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByMessageIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/messages/{message%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Message:
		"""
		Get messages from users
		The messages in a mailbox or folder. Read-only. Nullable.
		"""
		tags = ['users.message']

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
		return await self.request_adapter.send_async(request_info, Message, error_mapping)

	async def patch(
		self,
		body: Message,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Message:
		"""
		Update the navigation property messages in users
		
		"""
		tags = ['users.message']

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
		return await self.request_adapter.send_async(request_info, Message, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property messages for users
		
		"""
		tags = ['users.message']
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
		includeHiddenMessages: str = Field(default=None,serialization_alias="includeHiddenMessages")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> ByMessageIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByMessageIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByMessageIdRequest(self.request_adapter, self.path_parameters)

	@property
	def value(self,
	) -> ValueRequest:
		from .value import ValueRequest
		return ValueRequest(self.request_adapter, self.path_parameters)

	@property
	def attachments(self,
	) -> AttachmentsRequest:
		from .attachments import AttachmentsRequest
		return AttachmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def extensions(self,
	) -> ExtensionsRequest:
		from .extensions import ExtensionsRequest
		return ExtensionsRequest(self.request_adapter, self.path_parameters)

	@property
	def copy(self,
	) -> CopyRequest:
		from .copy import CopyRequest
		return CopyRequest(self.request_adapter, self.path_parameters)

	@property
	def create_forward(self,
	) -> CreateForwardRequest:
		from .create_forward import CreateForwardRequest
		return CreateForwardRequest(self.request_adapter, self.path_parameters)

	@property
	def create_reply(self,
	) -> CreateReplyRequest:
		from .create_reply import CreateReplyRequest
		return CreateReplyRequest(self.request_adapter, self.path_parameters)

	@property
	def create_reply_all(self,
	) -> CreateReplyAllRequest:
		from .create_reply_all import CreateReplyAllRequest
		return CreateReplyAllRequest(self.request_adapter, self.path_parameters)

	@property
	def forward(self,
	) -> ForwardRequest:
		from .forward import ForwardRequest
		return ForwardRequest(self.request_adapter, self.path_parameters)

	@property
	def move(self,
	) -> MoveRequest:
		from .move import MoveRequest
		return MoveRequest(self.request_adapter, self.path_parameters)

	@property
	def reply(self,
	) -> ReplyRequest:
		from .reply import ReplyRequest
		return ReplyRequest(self.request_adapter, self.path_parameters)

	@property
	def reply_all(self,
	) -> ReplyAllRequest:
		from .reply_all import ReplyAllRequest
		return ReplyAllRequest(self.request_adapter, self.path_parameters)

	@property
	def send(self,
	) -> SendRequest:
		from .send import SendRequest
		return SendRequest(self.request_adapter, self.path_parameters)

