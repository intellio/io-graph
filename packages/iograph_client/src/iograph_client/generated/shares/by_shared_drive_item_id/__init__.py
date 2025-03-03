# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .site import SiteRequest
	from .root import RootRequest
	from .permission import PermissionRequest
	from .list_item import ListItemRequest
	from .list import ListRequest
	from .last_modified_by_user import LastModifiedByUserRequest
	from .items import ItemsRequest
	from .drive_item import DriveItemRequest
	from .created_by_user import CreatedByUserRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.shared_drive_item import SharedDriveItem
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class BySharedDriveItemIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/shares/{sharedDriveItem%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SharedDriveItem:
		"""
		Accessing shared DriveItems
		Access a shared DriveItem or a collection of shared items by using a shareId or sharing URL. To use a sharing URL with this API, your app needs to transform the URL into a sharing token.
		Find more info here: https://learn.microsoft.com/graph/api/shares-get?view=graph-rest-1.0
		"""
		tags = ['shares.sharedDriveItem']

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
		return await self.request_adapter.send_async(request_info, SharedDriveItem, error_mapping)

	async def patch(
		self,
		body: SharedDriveItem,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SharedDriveItem:
		"""
		Update entity in shares
		
		"""
		tags = ['shares.sharedDriveItem']

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
		return await self.request_adapter.send_async(request_info, SharedDriveItem, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete entity from shares
		
		"""
		tags = ['shares.sharedDriveItem']
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



	def with_url(self, raw_url: str) -> BySharedDriveItemIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BySharedDriveItemIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BySharedDriveItemIdRequest(self.request_adapter, self.path_parameters)

	@property
	def created_by_user(self,
	) -> CreatedByUserRequest:
		from .created_by_user import CreatedByUserRequest
		return CreatedByUserRequest(self.request_adapter, self.path_parameters)

	@property
	def drive_item(self,
	) -> DriveItemRequest:
		from .drive_item import DriveItemRequest
		return DriveItemRequest(self.request_adapter, self.path_parameters)

	@property
	def items(self,
	) -> ItemsRequest:
		from .items import ItemsRequest
		return ItemsRequest(self.request_adapter, self.path_parameters)

	@property
	def last_modified_by_user(self,
	) -> LastModifiedByUserRequest:
		from .last_modified_by_user import LastModifiedByUserRequest
		return LastModifiedByUserRequest(self.request_adapter, self.path_parameters)

	@property
	def list(self,
	) -> ListRequest:
		from .list import ListRequest
		return ListRequest(self.request_adapter, self.path_parameters)

	@property
	def list_item(self,
	) -> ListItemRequest:
		from .list_item import ListItemRequest
		return ListItemRequest(self.request_adapter, self.path_parameters)

	@property
	def permission(self,
	) -> PermissionRequest:
		from .permission import PermissionRequest
		return PermissionRequest(self.request_adapter, self.path_parameters)

	@property
	def root(self,
	) -> RootRequest:
		from .root import RootRequest
		return RootRequest(self.request_adapter, self.path_parameters)

	@property
	def site(self,
	) -> SiteRequest:
		from .site import SiteRequest
		return SiteRequest(self.request_adapter, self.path_parameters)

