# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
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
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.message import Message
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByMessageIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/me/messages/{message%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Message:
		"""
		Get message
		Retrieve the properties and relationships of a message object. You can use the $value parameter to get the MIME content of a message. See also an example below. There are two scenarios where an app can get a message in another user's mail folder: Since the message resource supports extensions, you can also use the GET operation to get custom properties and extension data in a message instance.
		Find more info here: https://learn.microsoft.com/graph/api/message-get?view=graph-rest-1.0
		"""
		tags = ['me.message']

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
		Update message
		Update the properties of a message object.
		Find more info here: https://learn.microsoft.com/graph/api/message-update?view=graph-rest-1.0
		"""
		tags = ['me.message']

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
		Delete message
		Delete a message in the specified user's mailbox, or delete a relationship of the message.
		Find more info here: https://learn.microsoft.com/graph/api/message-delete?view=graph-rest-1.0
		"""
		tags = ['me.message']
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

