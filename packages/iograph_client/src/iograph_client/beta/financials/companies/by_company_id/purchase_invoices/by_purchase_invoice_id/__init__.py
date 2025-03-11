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
	from .vendor import VendorRequest
	from .purchase_invoice_lines import PurchaseInvoiceLinesRequest
	from .post import PostRequest
	from .currency import CurrencyRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.purchase_invoice import PurchaseInvoice


class ByPurchaseInvoiceIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/financials/companies/{company%2Did}/purchaseInvoices/{purchaseInvoice%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PurchaseInvoice:
		"""
		Get purchaseInvoices from financials
		
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
		return await self.request_adapter.send_async(request_info, PurchaseInvoice, error_mapping)

	async def patch(
		self,
		body: PurchaseInvoice,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PurchaseInvoice:
		"""
		Update the navigation property purchaseInvoices in financials
		
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
		return await self.request_adapter.send_async(request_info, PurchaseInvoice, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ByPurchaseInvoiceIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPurchaseInvoiceIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPurchaseInvoiceIdRequest(self.request_adapter, self.path_parameters)

	def currency(self,
		company_id: UUID,
		purchaseInvoice_id: UUID,
	) -> CurrencyRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if purchaseInvoice_id is None:
			raise TypeError("purchaseInvoice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["purchaseInvoice%2Did"] =  purchaseInvoice_id

		from .currency import CurrencyRequest
		return CurrencyRequest(self.request_adapter, path_parameters)

	def post(self,
		company_id: UUID,
		purchaseInvoice_id: UUID,
	) -> PostRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if purchaseInvoice_id is None:
			raise TypeError("purchaseInvoice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["purchaseInvoice%2Did"] =  purchaseInvoice_id

		from .post import PostRequest
		return PostRequest(self.request_adapter, path_parameters)

	def purchase_invoice_lines(self,
		company_id: UUID,
		purchaseInvoice_id: UUID,
	) -> PurchaseInvoiceLinesRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if purchaseInvoice_id is None:
			raise TypeError("purchaseInvoice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["purchaseInvoice%2Did"] =  purchaseInvoice_id

		from .purchase_invoice_lines import PurchaseInvoiceLinesRequest
		return PurchaseInvoiceLinesRequest(self.request_adapter, path_parameters)

	def vendor(self,
		company_id: UUID,
		purchaseInvoice_id: UUID,
	) -> VendorRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if purchaseInvoice_id is None:
			raise TypeError("purchaseInvoice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["purchaseInvoice%2Did"] =  purchaseInvoice_id

		from .vendor import VendorRequest
		return VendorRequest(self.request_adapter, path_parameters)

