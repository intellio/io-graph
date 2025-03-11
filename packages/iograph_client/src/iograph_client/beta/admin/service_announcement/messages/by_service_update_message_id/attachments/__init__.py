# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_service_announcement_attachment_id import ByServiceAnnouncementAttachmentIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.service_announcement_attachment import ServiceAnnouncementAttachment
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.service_announcement_attachment_collection_response import ServiceAnnouncementAttachmentCollectionResponse


class AttachmentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/serviceAnnouncement/messages/{serviceUpdateMessage%2Did}/attachments", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ServiceAnnouncementAttachmentCollectionResponse:
		"""
		List attachments
		Get a list of attachments associated with a service message.
		Find more info here: https://learn.microsoft.com/graph/api/serviceupdatemessage-list-attachments?view=graph-rest-beta
		"""
		tags = ['admin.serviceAnnouncement']

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
		return await self.request_adapter.send_async(request_info, ServiceAnnouncementAttachmentCollectionResponse, error_mapping)

	async def post(
		self,
		body: ServiceAnnouncementAttachment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ServiceAnnouncementAttachment:
		"""
		Create new navigation property to attachments for admin
		
		"""
		tags = ['admin.serviceAnnouncement']

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
		return await self.request_adapter.send_async(request_info, ServiceAnnouncementAttachment, error_mapping)

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

	def by_service_announcement_attachment_id(self,
		serviceUpdateMessage_id: str,
		serviceAnnouncementAttachment_id: str,
	) -> ByServiceAnnouncementAttachmentIdRequest:
		if serviceUpdateMessage_id is None:
			raise TypeError("serviceUpdateMessage_id cannot be null.")
		if serviceAnnouncementAttachment_id is None:
			raise TypeError("serviceAnnouncementAttachment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["serviceUpdateMessage%2Did"] =  serviceUpdateMessage_id
		path_parameters["serviceAnnouncementAttachment%2Did"] =  serviceAnnouncementAttachment_id

		from .by_service_announcement_attachment_id import ByServiceAnnouncementAttachmentIdRequest
		return ByServiceAnnouncementAttachmentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		serviceUpdateMessage_id: str,
	) -> CountRequest:
		if serviceUpdateMessage_id is None:
			raise TypeError("serviceUpdateMessage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["serviceUpdateMessage%2Did"] =  serviceUpdateMessage_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

