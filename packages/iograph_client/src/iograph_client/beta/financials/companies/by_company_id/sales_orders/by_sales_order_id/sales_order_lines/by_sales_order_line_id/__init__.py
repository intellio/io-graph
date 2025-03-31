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
	from .item import ItemRequest
	from .account import AccountRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.sales_order_line import SalesOrderLine
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class BySalesOrderLineIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/financials/companies/{company%2Did}/salesOrders/{salesOrder%2Did}/salesOrderLines/{salesOrderLine%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SalesOrderLine:
		"""
		Get salesOrderLines from financials
		
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
		return await self.request_adapter.send_async(request_info, SalesOrderLine, error_mapping)

	async def patch(
		self,
		body: SalesOrderLine,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SalesOrderLine:
		"""
		Update the navigation property salesOrderLines in financials
		
		"""
		tags = ['financials.company']

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
		return await self.request_adapter.send_async(request_info, SalesOrderLine, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> BySalesOrderLineIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BySalesOrderLineIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BySalesOrderLineIdRequest(self.request_adapter, self.path_parameters)

	def account(self,
		company_id: UUID,
		salesOrder_id: UUID,
		salesOrderLine_id: str,
	) -> AccountRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if salesOrder_id is None:
			raise TypeError("salesOrder_id cannot be null.")
		if salesOrderLine_id is None:
			raise TypeError("salesOrderLine_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["salesOrder%2Did"] =  salesOrder_id
		path_parameters["salesOrderLine%2Did"] =  salesOrderLine_id

		from .account import AccountRequest
		return AccountRequest(self.request_adapter, path_parameters)

	def item(self,
		company_id: UUID,
		salesOrder_id: UUID,
		salesOrderLine_id: str,
	) -> ItemRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if salesOrder_id is None:
			raise TypeError("salesOrder_id cannot be null.")
		if salesOrderLine_id is None:
			raise TypeError("salesOrderLine_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["salesOrder%2Did"] =  salesOrder_id
		path_parameters["salesOrderLine%2Did"] =  salesOrderLine_id

		from .item import ItemRequest
		return ItemRequest(self.request_adapter, path_parameters)

