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
	from .item import ItemRequest
	from .account import AccountRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.sales_invoice_line import SalesInvoiceLine
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class BySalesInvoiceLineIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/financials/companies/{company%2Did}/salesInvoiceLines/{salesInvoiceLine%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SalesInvoiceLine:
		"""
		Get salesInvoiceLines from financials
		
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
		return await self.request_adapter.send_async(request_info, SalesInvoiceLine, error_mapping)

	async def patch(
		self,
		body: SalesInvoiceLine,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SalesInvoiceLine:
		"""
		Update the navigation property salesInvoiceLines in financials
		
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
		return await self.request_adapter.send_async(request_info, SalesInvoiceLine, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> BySalesInvoiceLineIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: BySalesInvoiceLineIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return BySalesInvoiceLineIdRequest(self.request_adapter, self.path_parameters)

	def account(self,
		company_id: UUID,
		salesInvoiceLine_id: str,
	) -> AccountRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if salesInvoiceLine_id is None:
			raise TypeError("salesInvoiceLine_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["salesInvoiceLine%2Did"] =  salesInvoiceLine_id

		from .account import AccountRequest
		return AccountRequest(self.request_adapter, path_parameters)

	def item(self,
		company_id: UUID,
		salesInvoiceLine_id: str,
	) -> ItemRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")
		if salesInvoiceLine_id is None:
			raise TypeError("salesInvoiceLine_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id
		path_parameters["salesInvoiceLine%2Did"] =  salesInvoiceLine_id

		from .item import ItemRequest
		return ItemRequest(self.request_adapter, path_parameters)

