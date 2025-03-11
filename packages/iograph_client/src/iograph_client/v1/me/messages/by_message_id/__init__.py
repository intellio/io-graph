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
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.message import Message


class ByMessageIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/messages/{message%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Message:
		"""
		Get singleValueLegacyExtendedProperty
		You can get a single resource instance expanded with a specific extended property, or a collection of resource instances
that include extended properties matching a filter. Using the query parameter $expand allows you to get the specified resource instance expanded with a specific extended
property. Use a $filter and eq operator on the id property to specify the extended property. This is currently the only way to get the singleValueLegacyExtendedProperty object that represents an extended property. To get resource instances that have certain extended properties, use the $filter query parameter and apply an eq operator
on the id property. In addition, for numeric extended properties, apply one of the following operators on the value property:
eq, ne,ge, gt, le, or lt. For string-typed extended properties, apply a contains, startswith, eq, or ne operator on value. The filter is applied to all instances of the resource in the signed-in user's mailbox. Filtering the string name (Name) in the id of an extended property is case-sensitive. Filtering the value property of an extended
property is case-insensitive. The following user resources are supported: As well as the following group resources: See Extended properties overview for more information about when to use
open extensions or extended properties, and how to specify extended properties.
		Find more info here: https://learn.microsoft.com/graph/api/singlevaluelegacyextendedproperty-get?view=graph-rest-1.0
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



	def with_url(self, raw_url: str) -> ByMessageIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByMessageIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByMessageIdRequest(self.request_adapter, self.path_parameters)

	def value(self,
		message_id: str,
	) -> ValueRequest:
		if message_id is None:
			raise TypeError("message_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["message%2Did"] =  message_id

		from .value import ValueRequest
		return ValueRequest(self.request_adapter, path_parameters)

	def attachments(self,
		message_id: str,
	) -> AttachmentsRequest:
		if message_id is None:
			raise TypeError("message_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["message%2Did"] =  message_id

		from .attachments import AttachmentsRequest
		return AttachmentsRequest(self.request_adapter, path_parameters)

	def extensions(self,
		message_id: str,
	) -> ExtensionsRequest:
		if message_id is None:
			raise TypeError("message_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["message%2Did"] =  message_id

		from .extensions import ExtensionsRequest
		return ExtensionsRequest(self.request_adapter, path_parameters)

	def copy(self,
		message_id: str,
	) -> CopyRequest:
		if message_id is None:
			raise TypeError("message_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["message%2Did"] =  message_id

		from .copy import CopyRequest
		return CopyRequest(self.request_adapter, path_parameters)

	def create_forward(self,
		message_id: str,
	) -> CreateForwardRequest:
		if message_id is None:
			raise TypeError("message_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["message%2Did"] =  message_id

		from .create_forward import CreateForwardRequest
		return CreateForwardRequest(self.request_adapter, path_parameters)

	def create_reply(self,
		message_id: str,
	) -> CreateReplyRequest:
		if message_id is None:
			raise TypeError("message_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["message%2Did"] =  message_id

		from .create_reply import CreateReplyRequest
		return CreateReplyRequest(self.request_adapter, path_parameters)

	def create_reply_all(self,
		message_id: str,
	) -> CreateReplyAllRequest:
		if message_id is None:
			raise TypeError("message_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["message%2Did"] =  message_id

		from .create_reply_all import CreateReplyAllRequest
		return CreateReplyAllRequest(self.request_adapter, path_parameters)

	def forward(self,
		message_id: str,
	) -> ForwardRequest:
		if message_id is None:
			raise TypeError("message_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["message%2Did"] =  message_id

		from .forward import ForwardRequest
		return ForwardRequest(self.request_adapter, path_parameters)

	def move(self,
		message_id: str,
	) -> MoveRequest:
		if message_id is None:
			raise TypeError("message_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["message%2Did"] =  message_id

		from .move import MoveRequest
		return MoveRequest(self.request_adapter, path_parameters)

	def reply(self,
		message_id: str,
	) -> ReplyRequest:
		if message_id is None:
			raise TypeError("message_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["message%2Did"] =  message_id

		from .reply import ReplyRequest
		return ReplyRequest(self.request_adapter, path_parameters)

	def reply_all(self,
		message_id: str,
	) -> ReplyAllRequest:
		if message_id is None:
			raise TypeError("message_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["message%2Did"] =  message_id

		from .reply_all import ReplyAllRequest
		return ReplyAllRequest(self.request_adapter, path_parameters)

	def send(self,
		message_id: str,
	) -> SendRequest:
		if message_id is None:
			raise TypeError("message_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["message%2Did"] =  message_id

		from .send import SendRequest
		return SendRequest(self.request_adapter, path_parameters)

