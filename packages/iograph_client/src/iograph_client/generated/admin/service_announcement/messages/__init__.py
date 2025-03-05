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
	from .unfavorite import UnfavoriteRequest
	from .unarchive import UnarchiveRequest
	from .mark_unread import MarkUnreadRequest
	from .mark_read import MarkReadRequest
	from .favorite import FavoriteRequest
	from .archive import ArchiveRequest
	from .count import CountRequest
	from .by_service_update_message_id import ByServiceUpdateMessageIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.service_update_message_collection_response import ServiceUpdateMessageCollectionResponse
from iograph_models.models.service_update_message import ServiceUpdateMessage


class MessagesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/serviceAnnouncement/messages", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ServiceUpdateMessageCollectionResponse:
		"""
		List serviceAnnouncement messages
		Retrieve the serviceUpdateMessage resources from the messages navigation property. This operation retrieves all service update messages that exist for the tenant.
		Find more info here: https://learn.microsoft.com/graph/api/serviceannouncement-list-messages?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, ServiceUpdateMessageCollectionResponse, error_mapping)

	async def post(
		self,
		body: ServiceUpdateMessage,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ServiceUpdateMessage:
		"""
		Create new navigation property to messages for admin
		
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
		return await self.request_adapter.send_async(request_info, ServiceUpdateMessage, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> MessagesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MessagesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MessagesRequest(self.request_adapter, self.path_parameters)

	def by_service_update_message_id(self,
		serviceUpdateMessage_id: str,
	) -> ByServiceUpdateMessageIdRequest:
		if serviceUpdateMessage_id is None:
			raise TypeError("serviceUpdateMessage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["serviceUpdateMessage%2Did"] =  serviceUpdateMessage_id

		from .by_service_update_message_id import ByServiceUpdateMessageIdRequest
		return ByServiceUpdateMessageIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def archive(self,
	) -> ArchiveRequest:
		from .archive import ArchiveRequest
		return ArchiveRequest(self.request_adapter, self.path_parameters)

	@property
	def favorite(self,
	) -> FavoriteRequest:
		from .favorite import FavoriteRequest
		return FavoriteRequest(self.request_adapter, self.path_parameters)

	@property
	def mark_read(self,
	) -> MarkReadRequest:
		from .mark_read import MarkReadRequest
		return MarkReadRequest(self.request_adapter, self.path_parameters)

	@property
	def mark_unread(self,
	) -> MarkUnreadRequest:
		from .mark_unread import MarkUnreadRequest
		return MarkUnreadRequest(self.request_adapter, self.path_parameters)

	@property
	def unarchive(self,
	) -> UnarchiveRequest:
		from .unarchive import UnarchiveRequest
		return UnarchiveRequest(self.request_adapter, self.path_parameters)

	@property
	def unfavorite(self,
	) -> UnfavoriteRequest:
		from .unfavorite import UnfavoriteRequest
		return UnfavoriteRequest(self.request_adapter, self.path_parameters)

