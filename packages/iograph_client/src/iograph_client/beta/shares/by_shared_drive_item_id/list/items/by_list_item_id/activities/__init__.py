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
	from .by_item_activity_o_l_d_id import ByItemActivityOLDIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.item_activity_o_l_d_collection_response import ItemActivityOLDCollectionResponse
from iograph_models.beta.item_activity_o_l_d import ItemActivityOLD
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ActivitiesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/shares/{sharedDriveItem%2Did}/list/items/{listItem%2Did}/activities", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ItemActivityOLDCollectionResponse:
		"""
		Get activities from shares
		The list of recent activities that took place on this item.
		"""
		tags = ['shares.list']

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
		return await self.request_adapter.send_async(request_info, ItemActivityOLDCollectionResponse, error_mapping)

	async def post(
		self,
		body: ItemActivityOLD,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ItemActivityOLD:
		"""
		Create new navigation property to activities for shares
		
		"""
		tags = ['shares.list']

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
		return await self.request_adapter.send_async(request_info, ItemActivityOLD, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ActivitiesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ActivitiesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ActivitiesRequest(self.request_adapter, self.path_parameters)

	def by_item_activity_o_l_d_id(self,
		sharedDriveItem_id: str,
		listItem_id: str,
		itemActivityOLD_id: str,
	) -> ByItemActivityOLDIdRequest:
		if sharedDriveItem_id is None:
			raise TypeError("sharedDriveItem_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")
		if itemActivityOLD_id is None:
			raise TypeError("itemActivityOLD_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sharedDriveItem%2Did"] =  sharedDriveItem_id
		path_parameters["listItem%2Did"] =  listItem_id
		path_parameters["itemActivityOLD%2Did"] =  itemActivityOLD_id

		from .by_item_activity_o_l_d_id import ByItemActivityOLDIdRequest
		return ByItemActivityOLDIdRequest(self.request_adapter, path_parameters)

	def count(self,
		sharedDriveItem_id: str,
		listItem_id: str,
	) -> CountRequest:
		if sharedDriveItem_id is None:
			raise TypeError("sharedDriveItem_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sharedDriveItem%2Did"] =  sharedDriveItem_id
		path_parameters["listItem%2Did"] =  listItem_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

