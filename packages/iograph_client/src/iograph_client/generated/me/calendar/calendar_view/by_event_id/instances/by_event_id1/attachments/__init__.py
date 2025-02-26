# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .create_upload_session import CreateUploadSessionRequest
	from .count import CountRequest
	from .by_attachment_id import ByAttachmentIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.models.attachment import Attachment
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.attachment_collection_response import AttachmentCollectionResponse


class AttachmentsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/me/calendar/calendarView/{event%2Did}/instances/{event%2Did1}/attachments"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AttachmentCollectionResponse:
		"""
		Get attachments from me
		The collection of FileAttachment, ItemAttachment, and referenceAttachment attachments for the event. Navigation property. Read-only. Nullable.
		"""
		tags = ['me.calendar']

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
		Create new navigation property to attachments for me
		
		"""
		tags = ['me.calendar']

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


	def by_attachment_id(self,
		event_id: str,
		event_id1: str,
		attachment_id: str,
	) -> ByAttachmentIdRequest:
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")
		if attachment_id is None:
			raise TypeError("attachment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1
		path_parameters["attachment%2Did"] =  attachment_id

		from .by_attachment_id import ByAttachmentIdRequest
		return ByAttachmentIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def create_upload_session(self,
	) -> CreateUploadSessionRequest:
		from .create_upload_session import CreateUploadSessionRequest
		return CreateUploadSessionRequest(self.request_adapter, self.path_parameters)

