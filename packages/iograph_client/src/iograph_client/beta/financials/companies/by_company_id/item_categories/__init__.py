# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_item_category_id import ByItemCategoryIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.item_category_collection_response import ItemCategoryCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.item_category import ItemCategory


class ItemCategoriesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/financials/companies/{company%2Did}/itemCategories", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ItemCategoryCollectionResponse:
		"""
		Get itemCategories from financials
		
		"""
		tags = ['financials.company']

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
		return await self.request_adapter.send_async(request_info, ItemCategoryCollectionResponse, error_mapping)

	async def post(
		self,
		body: ItemCategory,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ItemCategory:
		"""
		Create new navigation property to itemCategories for financials
		
		"""
		tags = ['financials.company']

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
		return await self.request_adapter.send_async(request_info, ItemCategory, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ItemCategoriesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ItemCategoriesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ItemCategoriesRequest(self.request_adapter, self.path_parameters)

	def by_item_category_id(self,
		company_id: UUID,
		itemCategory_id: UUID,
	) -> ByItemCategoryIdRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if itemCategory_id is None:
			raise TypeError("itemCategory_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["itemCategory%2Did"] =  itemCategory_id

		from .by_item_category_id import ByItemCategoryIdRequest
		return ByItemCategoryIdRequest(self.request_adapter, path_parameters)

	def count(self,
		company_id: UUID,
	) -> CountRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

