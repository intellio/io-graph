# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .create_upload_session import CreateUploadSessionRequest
	from .count import CountRequest
	from .by_attachment_id import ByAttachmentIdRequest
	from ...........request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.attachment_collection_response import AttachmentCollectionResponse
from iograph_models.v1.attachment import Attachment


class AttachmentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/conversations/{conversation%2Did}/threads/{conversationThread%2Did}/posts/{post%2Did}/attachments", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AttachmentCollectionResponse:
		"""
		Get attachments from groups
		Read-only. Nullable. Supports $expand.
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
		return await self.request_adapter.send_async(request_info, AttachmentCollectionResponse, error_mapping)

	async def post(
		self,
		body: Attachment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Attachment:
		"""
		Create new navigation property to attachments for groups
		
		"""
		tags = ['groups.conversation']

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
		return await self.request_adapter.send_async(request_info, Attachment, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AttachmentsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AttachmentsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AttachmentsRequest(self.request_adapter, self.path_parameters)

	def by_attachment_id(self,
		group_id: str,
		conversation_id: str,
		conversationThread_id: str,
		post_id: str,
		attachment_id: str,
	) -> ByAttachmentIdRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if conversation_id is None:
			raise TypeError("conversation_id cannot be null.")
		if conversationThread_id is None:
			raise TypeError("conversationThread_id cannot be null.")
		if post_id is None:
			raise TypeError("post_id cannot be null.")
		if attachment_id is None:
			raise TypeError("attachment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["conversation%2Did"] =  conversation_id
		path_parameters["conversationThread%2Did"] =  conversationThread_id
		path_parameters["post%2Did"] =  post_id
		path_parameters["attachment%2Did"] =  attachment_id

		from .by_attachment_id import ByAttachmentIdRequest
		return ByAttachmentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		group_id: str,
		conversation_id: str,
		conversationThread_id: str,
		post_id: str,
	) -> CountRequest:
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

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def create_upload_session(self,
		group_id: str,
		conversation_id: str,
		conversationThread_id: str,
		post_id: str,
	) -> CreateUploadSessionRequest:
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

		from .create_upload_session import CreateUploadSessionRequest
		return CreateUploadSessionRequest(self.request_adapter, path_parameters)

