# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .............request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .create_upload_session import CreateUploadSessionRequest
	from .count import CountRequest
	from .by_attachment_id import ByAttachmentIdRequest
	from .............request_adapter import HttpxRequestAdapter
from iograph_models.beta.attachment_collection_response import AttachmentCollectionResponse
from iograph_models.beta.attachment import Attachment
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class AttachmentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/calendars/{calendar%2Did}/events/{event%2Did}/instances/{event%2Did1}/exceptionOccurrences/{event%2Did2}/attachments", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AttachmentCollectionResponse:
		"""
		Get attachments from users
		The collection of FileAttachment, ItemAttachment, and referenceAttachment attachments for the event. Navigation property. Read-only. Nullable.
		"""
		tags = ['users.calendar']

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
		Create new navigation property to attachments for users
		
		"""
		tags = ['users.calendar']

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
		user_id: str,
		calendar_id: str,
		event_id: str,
		event_id1: str,
		event_id2: str,
		attachment_id: str,
	) -> ByAttachmentIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")
		if event_id2 is None:
			raise TypeError("event_id2 cannot be null.")
		if attachment_id is None:
			raise TypeError("attachment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1
		path_parameters["event%2Did2"] =  event_id2
		path_parameters["attachment%2Did"] =  attachment_id

		from .by_attachment_id import ByAttachmentIdRequest
		return ByAttachmentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
		calendar_id: str,
		event_id: str,
		event_id1: str,
		event_id2: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")
		if event_id2 is None:
			raise TypeError("event_id2 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1
		path_parameters["event%2Did2"] =  event_id2

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def create_upload_session(self,
		user_id: str,
		calendar_id: str,
		event_id: str,
		event_id1: str,
		event_id2: str,
	) -> CreateUploadSessionRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if calendar_id is None:
			raise TypeError("calendar_id cannot be null.")
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")
		if event_id2 is None:
			raise TypeError("event_id2 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["calendar%2Did"] =  calendar_id
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1
		path_parameters["event%2Did2"] =  event_id2

		from .create_upload_session import CreateUploadSessionRequest
		return CreateUploadSessionRequest(self.request_adapter, path_parameters)

