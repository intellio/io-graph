# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .list_item import ListItemRequest
	from .drive_item import DriveItemRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.item_activity_o_l_d import ItemActivityOLD


class ByItemActivityOLDIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/list/items/{listItem%2Did}/activities/{itemActivityOLD%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ItemActivityOLD:
		"""
		Get activities from drives
		The list of recent activities that took place on this item.
		"""
		tags = ['drives.list']

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
		return await self.request_adapter.send_async(request_info, ItemActivityOLD, error_mapping)

	async def patch(
		self,
		body: ItemActivityOLD,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ItemActivityOLD:
		"""
		Update the navigation property activities in drives
		
		"""
		tags = ['drives.list']

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
		return await self.request_adapter.send_async(request_info, ItemActivityOLD, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property activities for drives
		
		"""
		tags = ['drives.list']
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



	def with_url(self, raw_url: str) -> ByItemActivityOLDIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByItemActivityOLDIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByItemActivityOLDIdRequest(self.request_adapter, self.path_parameters)

	def drive_item(self,
		drive_id: str,
		listItem_id: str,
		itemActivityOLD_id: str,
	) -> DriveItemRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")
		if itemActivityOLD_id is None:
			raise TypeError("itemActivityOLD_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["listItem%2Did"] =  listItem_id
		path_parameters["itemActivityOLD%2Did"] =  itemActivityOLD_id

		from .drive_item import DriveItemRequest
		return DriveItemRequest(self.request_adapter, path_parameters)

	def list_item(self,
		drive_id: str,
		listItem_id: str,
		itemActivityOLD_id: str,
	) -> ListItemRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")
		if itemActivityOLD_id is None:
			raise TypeError("itemActivityOLD_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["listItem%2Did"] =  listItem_id
		path_parameters["itemActivityOLD%2Did"] =  itemActivityOLD_id

		from .list_item import ListItemRequest
		return ListItemRequest(self.request_adapter, path_parameters)

