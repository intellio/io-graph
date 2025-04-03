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
	from .windows_updates_find_by_kb_number_with_kbnumber import WindowsUpdatesFindByKbNumberWithKbNumberRequest
	from .windows_updates_find_by_catalog_id_with_catalogid import WindowsUpdatesFindByCatalogIdWithCatalogIDRequest
	from .count import CountRequest
	from .by_product_id import ByProductIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.windows_updates_product import WindowsUpdatesProduct
from iograph_models.beta.windows_updates_product_collection_response import WindowsUpdatesProductCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ProductsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/windows/updates/products", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WindowsUpdatesProductCollectionResponse:
		"""
		Get products from admin
		A collection of Windows products.
		"""
		tags = ['admin.adminWindows']

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
		return await self.request_adapter.send_async(request_info, WindowsUpdatesProductCollectionResponse, error_mapping)

	async def post(
		self,
		body: WindowsUpdatesProduct,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WindowsUpdatesProduct:
		"""
		Create new navigation property to products for admin
		
		"""
		tags = ['admin.adminWindows']

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
		return await self.request_adapter.send_async(request_info, WindowsUpdatesProduct, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ProductsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ProductsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ProductsRequest(self.request_adapter, self.path_parameters)

	def by_product_id(self,
		product_id: str,
	) -> ByProductIdRequest:
		if product_id is None:
			raise TypeError("product_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["product%2Did"] =  product_id

		from .by_product_id import ByProductIdRequest
		return ByProductIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	def windows_updates_find_by_catalog_id_with_catalogid(self,
		catalogID: str,
	) -> WindowsUpdatesFindByCatalogIdWithCatalogIDRequest:
		if catalogID is None:
			raise TypeError("catalogID cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["catalogID"] =  catalogID

		from .windows_updates_find_by_catalog_id_with_catalogid import WindowsUpdatesFindByCatalogIdWithCatalogIDRequest
		return WindowsUpdatesFindByCatalogIdWithCatalogIDRequest(self.request_adapter, path_parameters)

	def windows_updates_find_by_kb_number_with_kbnumber(self,
		kbNumber: int,
	) -> WindowsUpdatesFindByKbNumberWithKbNumberRequest:
		if kbNumber is None:
			raise TypeError("kbNumber cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["kbNumber"] =  kbNumber

		from .windows_updates_find_by_kb_number_with_kbnumber import WindowsUpdatesFindByKbNumberWithKbNumberRequest
		return WindowsUpdatesFindByKbNumberWithKbNumberRequest(self.request_adapter, path_parameters)

