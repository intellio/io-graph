# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_message_id import ByMessageIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.message import Message
from iograph_models.models.message_collection_response import MessageCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class MessagesRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/me/messages"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MessageCollectionResponse:
		"""
		List messages
		Get the messages in the signed-in user's mailbox (including the Deleted Items and Clutter folders). Depending on the page size and mailbox data, getting messages from a mailbox can incur multiple requests. The default page size is 10 messages. Use $top to customize the page size, within the range of 1 and 1000. To improve the operation response time, use $select to specify the exact properties you need; see example 1 below. Fine-tune the values for $select and $top, especially when you must use a larger page size, as returning a page with hundreds of messages each with a full response payload may trigger the gateway timeout (HTTP 504). To get the next page of messages, simply apply the entire URL returned in @odata.nextLink to the next get-messages request. This URL includes any query parameters you may have specified in the initial request. Do not try to extract the $skip value from the @odata.nextLink URL to manipulate responses. This API uses the $skip value to keep count of all the items it has gone through in the user's mailbox to return a page of message-type items. It's therefore possible that even in the initial response, the $skip value is larger than the page size. For more information, see Paging Microsoft Graph data in your app. Currently, this operation returns message bodies in only HTML format. There are two scenarios where an app can get messages in another user's mail folder:
		Find more info here: https://learn.microsoft.com/graph/api/user-list-messages?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, MessageCollectionResponse, error_mapping)

	async def post(
		self,
		body: Message,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Message:
		"""
		Create message
		Create a draft of a new message in either JSON or MIME format. When using JSON format, you can:
- Include an attachment to the message.
- Update the draft later to add content to the body or change other message properties. When using MIME format:
- Provide the applicable Internet message headers and the MIME content, all encoded in base64 format in the request body.
- /* Add any attachments and S/MIME properties to the MIME content. By default, this operation saves the draft in the Drafts folder. Send the draft message in a subsequent operation. Alternatively, send a new message in a single operation, or create a draft to forward, reply and reply-all to an existing message.
		Find more info here: https://learn.microsoft.com/graph/api/user-post-messages?view=graph-rest-1.0
		"""
		tags = ['me.message']

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
		return await self.request_adapter.send_async(request_info, Message, error_mapping)

	class GetQueryParams(BaseModel):
		includeHiddenMessages: str = Field(default=None,serialization_alias="includeHiddenMessages")
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_message_id(self,
		message_id: str,
	) -> ByMessageIdRequest:
		if message_id is None:
			raise TypeError("message_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["message%2Did"] =  message_id

		from .by_message_id import ByMessageIdRequest
		return ByMessageIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

