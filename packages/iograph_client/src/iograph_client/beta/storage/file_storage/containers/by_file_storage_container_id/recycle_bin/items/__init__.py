# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_recycle_bin_item_id import ByRecycleBinItemIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.recycle_bin_item_collection_response import RecycleBinItemCollectionResponse
from iograph_models.beta.recycle_bin_item import RecycleBinItem


class ItemsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/storage/fileStorage/containers/{fileStorageContainer%2Did}/recycleBin/items", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> RecycleBinItemCollectionResponse:
		"""
		Get items from storage
		List of the recycleBinItems deleted by a user.
		"""
		tags = ['storage.fileStorage']

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
		return await self.request_adapter.send_async(request_info, RecycleBinItemCollectionResponse, error_mapping)

	async def post(
		self,
		body: RecycleBinItem,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> RecycleBinItem:
		"""
		Create new navigation property to items for storage
		
		"""
		tags = ['storage.fileStorage']

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
		return await self.request_adapter.send_async(request_info, RecycleBinItem, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ItemsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ItemsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ItemsRequest(self.request_adapter, self.path_parameters)

	def by_recycle_bin_item_id(self,
		fileStorageContainer_id: str,
		recycleBinItem_id: str,
	) -> ByRecycleBinItemIdRequest:
		if fileStorageContainer_id is None:
			raise TypeError("fileStorageContainer_id cannot be null.")
		if recycleBinItem_id is None:
			raise TypeError("recycleBinItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fileStorageContainer%2Did"] =  fileStorageContainer_id
		path_parameters["recycleBinItem%2Did"] =  recycleBinItem_id

		from .by_recycle_bin_item_id import ByRecycleBinItemIdRequest
		return ByRecycleBinItemIdRequest(self.request_adapter, path_parameters)

	def count(self,
		fileStorageContainer_id: str,
	) -> CountRequest:
		if fileStorageContainer_id is None:
			raise TypeError("fileStorageContainer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fileStorageContainer%2Did"] =  fileStorageContainer_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

