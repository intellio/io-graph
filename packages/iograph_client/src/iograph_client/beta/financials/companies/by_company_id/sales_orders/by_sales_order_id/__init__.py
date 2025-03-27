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
	from .sales_order_lines import SalesOrderLinesRequest
	from .payment_term import PaymentTermRequest
	from .customer import CustomerRequest
	from .currency import CurrencyRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.sales_order import SalesOrder
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class BySalesOrderIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/financials/companies/{company%2Did}/salesOrders/{salesOrder%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SalesOrder:
		"""
		Get salesOrders from financials
		
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
		return await self.request_adapter.send_async(request_info, SalesOrder, error_mapping)

	async def patch(
		self,
		body: SalesOrder,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SalesOrder:
		"""
		Update the navigation property salesOrders in financials
		
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
		return await self.request_adapter.send_async(request_info, SalesOrder, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> BySalesOrderIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BySalesOrderIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BySalesOrderIdRequest(self.request_adapter, self.path_parameters)

	def currency(self,
		company_id: UUID,
		salesOrder_id: UUID,
	) -> CurrencyRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if salesOrder_id is None:
			raise TypeError("salesOrder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["salesOrder%2Did"] =  salesOrder_id

		from .currency import CurrencyRequest
		return CurrencyRequest(self.request_adapter, path_parameters)

	def customer(self,
		company_id: UUID,
		salesOrder_id: UUID,
	) -> CustomerRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if salesOrder_id is None:
			raise TypeError("salesOrder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["salesOrder%2Did"] =  salesOrder_id

		from .customer import CustomerRequest
		return CustomerRequest(self.request_adapter, path_parameters)

	def payment_term(self,
		company_id: UUID,
		salesOrder_id: UUID,
	) -> PaymentTermRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if salesOrder_id is None:
			raise TypeError("salesOrder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["salesOrder%2Did"] =  salesOrder_id

		from .payment_term import PaymentTermRequest
		return PaymentTermRequest(self.request_adapter, path_parameters)

	def sales_order_lines(self,
		company_id: UUID,
		salesOrder_id: UUID,
	) -> SalesOrderLinesRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if salesOrder_id is None:
			raise TypeError("salesOrder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["salesOrder%2Did"] =  salesOrder_id

		from .sales_order_lines import SalesOrderLinesRequest
		return SalesOrderLinesRequest(self.request_adapter, path_parameters)

