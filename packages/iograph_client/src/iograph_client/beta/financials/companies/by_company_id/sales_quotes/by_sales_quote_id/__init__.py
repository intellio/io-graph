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
	from .shipment_method import ShipmentMethodRequest
	from .sales_quote_lines import SalesQuoteLinesRequest
	from .payment_term import PaymentTermRequest
	from .send import SendRequest
	from .make_invoice import MakeInvoiceRequest
	from .customer import CustomerRequest
	from .currency import CurrencyRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.sales_quote import SalesQuote


class BySalesQuoteIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/financials/companies/{company%2Did}/salesQuotes/{salesQuote%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SalesQuote:
		"""
		Get salesQuotes from financials
		
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
		return await self.request_adapter.send_async(request_info, SalesQuote, error_mapping)

	async def patch(
		self,
		body: SalesQuote,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SalesQuote:
		"""
		Update the navigation property salesQuotes in financials
		
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
		return await self.request_adapter.send_async(request_info, SalesQuote, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> BySalesQuoteIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BySalesQuoteIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BySalesQuoteIdRequest(self.request_adapter, self.path_parameters)

	def currency(self,
		company_id: UUID,
		salesQuote_id: UUID,
	) -> CurrencyRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if salesQuote_id is None:
			raise TypeError("salesQuote_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["salesQuote%2Did"] =  salesQuote_id

		from .currency import CurrencyRequest
		return CurrencyRequest(self.request_adapter, path_parameters)

	def customer(self,
		company_id: UUID,
		salesQuote_id: UUID,
	) -> CustomerRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if salesQuote_id is None:
			raise TypeError("salesQuote_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["salesQuote%2Did"] =  salesQuote_id

		from .customer import CustomerRequest
		return CustomerRequest(self.request_adapter, path_parameters)

	def make_invoice(self,
		company_id: UUID,
		salesQuote_id: UUID,
	) -> MakeInvoiceRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if salesQuote_id is None:
			raise TypeError("salesQuote_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["salesQuote%2Did"] =  salesQuote_id

		from .make_invoice import MakeInvoiceRequest
		return MakeInvoiceRequest(self.request_adapter, path_parameters)

	def send(self,
		company_id: UUID,
		salesQuote_id: UUID,
	) -> SendRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if salesQuote_id is None:
			raise TypeError("salesQuote_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["salesQuote%2Did"] =  salesQuote_id

		from .send import SendRequest
		return SendRequest(self.request_adapter, path_parameters)

	def payment_term(self,
		company_id: UUID,
		salesQuote_id: UUID,
	) -> PaymentTermRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if salesQuote_id is None:
			raise TypeError("salesQuote_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["salesQuote%2Did"] =  salesQuote_id

		from .payment_term import PaymentTermRequest
		return PaymentTermRequest(self.request_adapter, path_parameters)

	def sales_quote_lines(self,
		company_id: UUID,
		salesQuote_id: UUID,
	) -> SalesQuoteLinesRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if salesQuote_id is None:
			raise TypeError("salesQuote_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["salesQuote%2Did"] =  salesQuote_id

		from .sales_quote_lines import SalesQuoteLinesRequest
		return SalesQuoteLinesRequest(self.request_adapter, path_parameters)

	def shipment_method(self,
		company_id: UUID,
		salesQuote_id: UUID,
	) -> ShipmentMethodRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if salesQuote_id is None:
			raise TypeError("salesQuote_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["salesQuote%2Did"] =  salesQuote_id

		from .shipment_method import ShipmentMethodRequest
		return ShipmentMethodRequest(self.request_adapter, path_parameters)

