# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .reply import ReplyRequest
	from .forward import ForwardRequest
	from .in_reply_to import InReplyToRequest
	from .extensions import ExtensionsRequest
	from .attachments import AttachmentsRequest
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.models.post import Post
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByPostIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/conversations/{conversation%2Did}/threads/{conversationThread%2Did}/posts/{post%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Post:
		"""
		Get posts from groups
		
		"""
		tags = ['groups.conversation']

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
		return await self.request_adapter.send_async(request_info, Post, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ByPostIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPostIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPostIdRequest(self.request_adapter, self.path_parameters)

	def attachments(self,
		group_id: str,
		conversation_id: str,
		conversationThread_id: str,
		post_id: str,
	) -> AttachmentsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if conversation_id is None:
			raise TypeError("conversation_id cannot be null.")
		if conversationThread_id is None:
			raise TypeError("conversationThread_id cannot be null.")
		if post_id is None:
			raise TypeError("post_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["conversation%2Did"] =  conversation_id
		path_parameters["conversationThread%2Did"] =  conversationThread_id
		path_parameters["post%2Did"] =  post_id

		from .attachments import AttachmentsRequest
		return AttachmentsRequest(self.request_adapter, path_parameters)

	def extensions(self,
		group_id: str,
		conversation_id: str,
		conversationThread_id: str,
		post_id: str,
	) -> ExtensionsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if conversation_id is None:
			raise TypeError("conversation_id cannot be null.")
		if conversationThread_id is None:
			raise TypeError("conversationThread_id cannot be null.")
		if post_id is None:
			raise TypeError("post_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["conversation%2Did"] =  conversation_id
		path_parameters["conversationThread%2Did"] =  conversationThread_id
		path_parameters["post%2Did"] =  post_id

		from .extensions import ExtensionsRequest
		return ExtensionsRequest(self.request_adapter, path_parameters)

	def in_reply_to(self,
		group_id: str,
		conversation_id: str,
		conversationThread_id: str,
		post_id: str,
	) -> InReplyToRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if conversation_id is None:
			raise TypeError("conversation_id cannot be null.")
		if conversationThread_id is None:
			raise TypeError("conversationThread_id cannot be null.")
		if post_id is None:
			raise TypeError("post_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["conversation%2Did"] =  conversation_id
		path_parameters["conversationThread%2Did"] =  conversationThread_id
		path_parameters["post%2Did"] =  post_id

		from .in_reply_to import InReplyToRequest
		return InReplyToRequest(self.request_adapter, path_parameters)

	def forward(self,
		group_id: str,
		conversation_id: str,
		conversationThread_id: str,
		post_id: str,
	) -> ForwardRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if conversation_id is None:
			raise TypeError("conversation_id cannot be null.")
		if conversationThread_id is None:
			raise TypeError("conversationThread_id cannot be null.")
		if post_id is None:
			raise TypeError("post_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["conversation%2Did"] =  conversation_id
		path_parameters["conversationThread%2Did"] =  conversationThread_id
		path_parameters["post%2Did"] =  post_id

		from .forward import ForwardRequest
		return ForwardRequest(self.request_adapter, path_parameters)

	def reply(self,
		group_id: str,
		conversation_id: str,
		conversationThread_id: str,
		post_id: str,
	) -> ReplyRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if conversation_id is None:
			raise TypeError("conversation_id cannot be null.")
		if conversationThread_id is None:
			raise TypeError("conversationThread_id cannot be null.")
		if post_id is None:
			raise TypeError("post_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["conversation%2Did"] =  conversation_id
		path_parameters["conversationThread%2Did"] =  conversationThread_id
		path_parameters["post%2Did"] =  post_id

		from .reply import ReplyRequest
		return ReplyRequest(self.request_adapter, path_parameters)

