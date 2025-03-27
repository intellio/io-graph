# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .vendors import VendorsRequest
	from .units_of_measure import UnitsOfMeasureRequest
	from .tax_groups import TaxGroupsRequest
	from .tax_areas import TaxAreasRequest
	from .shipment_methods import ShipmentMethodsRequest
	from .sales_quotes import SalesQuotesRequest
	from .sales_quote_lines import SalesQuoteLinesRequest
	from .sales_orders import SalesOrdersRequest
	from .sales_order_lines import SalesOrderLinesRequest
	from .sales_invoices import SalesInvoicesRequest
	from .sales_invoice_lines import SalesInvoiceLinesRequest
	from .sales_credit_memos import SalesCreditMemosRequest
	from .sales_credit_memo_lines import SalesCreditMemoLinesRequest
	from .purchase_invoices import PurchaseInvoicesRequest
	from .purchase_invoice_lines import PurchaseInvoiceLinesRequest
	from .picture import PictureRequest
	from .payment_terms import PaymentTermsRequest
	from .payment_methods import PaymentMethodsRequest
	from .journals import JournalsRequest
	from .journal_lines import JournalLinesRequest
	from .items import ItemsRequest
	from .item_categories import ItemCategoriesRequest
	from .general_ledger_entries import GeneralLedgerEntriesRequest
	from .employees import EmployeesRequest
	from .dimension_values import DimensionValuesRequest
	from .dimensions import DimensionsRequest
	from .customers import CustomersRequest
	from .customer_payments import CustomerPaymentsRequest
	from .customer_payment_journals import CustomerPaymentJournalsRequest
	from .currencies import CurrenciesRequest
	from .countries_regions import CountriesRegionsRequest
	from .company_information import CompanyInformationRequest
	from .aged_accounts_receivable import AgedAccountsReceivableRequest
	from .aged_accounts_payable import AgedAccountsPayableRequest
	from .accounts import AccountsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.company import Company
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByCompanyIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/financials/companies/{company%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Company:
		"""
		Get companies from financials
		
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
		return await self.request_adapter.send_async(request_info, Company, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ByCompanyIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByCompanyIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByCompanyIdRequest(self.request_adapter, self.path_parameters)

	def accounts(self,
		company_id: UUID,
	) -> AccountsRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .accounts import AccountsRequest
		return AccountsRequest(self.request_adapter, path_parameters)

	def aged_accounts_payable(self,
		company_id: UUID,
	) -> AgedAccountsPayableRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .aged_accounts_payable import AgedAccountsPayableRequest
		return AgedAccountsPayableRequest(self.request_adapter, path_parameters)

	def aged_accounts_receivable(self,
		company_id: UUID,
	) -> AgedAccountsReceivableRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .aged_accounts_receivable import AgedAccountsReceivableRequest
		return AgedAccountsReceivableRequest(self.request_adapter, path_parameters)

	def company_information(self,
		company_id: UUID,
	) -> CompanyInformationRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .company_information import CompanyInformationRequest
		return CompanyInformationRequest(self.request_adapter, path_parameters)

	def countries_regions(self,
		company_id: UUID,
	) -> CountriesRegionsRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .countries_regions import CountriesRegionsRequest
		return CountriesRegionsRequest(self.request_adapter, path_parameters)

	def currencies(self,
		company_id: UUID,
	) -> CurrenciesRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .currencies import CurrenciesRequest
		return CurrenciesRequest(self.request_adapter, path_parameters)

	def customer_payment_journals(self,
		company_id: UUID,
	) -> CustomerPaymentJournalsRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .customer_payment_journals import CustomerPaymentJournalsRequest
		return CustomerPaymentJournalsRequest(self.request_adapter, path_parameters)

	def customer_payments(self,
		company_id: UUID,
	) -> CustomerPaymentsRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .customer_payments import CustomerPaymentsRequest
		return CustomerPaymentsRequest(self.request_adapter, path_parameters)

	def customers(self,
		company_id: UUID,
	) -> CustomersRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .customers import CustomersRequest
		return CustomersRequest(self.request_adapter, path_parameters)

	def dimensions(self,
		company_id: UUID,
	) -> DimensionsRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .dimensions import DimensionsRequest
		return DimensionsRequest(self.request_adapter, path_parameters)

	def dimension_values(self,
		company_id: UUID,
	) -> DimensionValuesRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .dimension_values import DimensionValuesRequest
		return DimensionValuesRequest(self.request_adapter, path_parameters)

	def employees(self,
		company_id: UUID,
	) -> EmployeesRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .employees import EmployeesRequest
		return EmployeesRequest(self.request_adapter, path_parameters)

	def general_ledger_entries(self,
		company_id: UUID,
	) -> GeneralLedgerEntriesRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .general_ledger_entries import GeneralLedgerEntriesRequest
		return GeneralLedgerEntriesRequest(self.request_adapter, path_parameters)

	def item_categories(self,
		company_id: UUID,
	) -> ItemCategoriesRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .item_categories import ItemCategoriesRequest
		return ItemCategoriesRequest(self.request_adapter, path_parameters)

	def items(self,
		company_id: UUID,
	) -> ItemsRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .items import ItemsRequest
		return ItemsRequest(self.request_adapter, path_parameters)

	def journal_lines(self,
		company_id: UUID,
	) -> JournalLinesRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .journal_lines import JournalLinesRequest
		return JournalLinesRequest(self.request_adapter, path_parameters)

	def journals(self,
		company_id: UUID,
	) -> JournalsRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .journals import JournalsRequest
		return JournalsRequest(self.request_adapter, path_parameters)

	def payment_methods(self,
		company_id: UUID,
	) -> PaymentMethodsRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .payment_methods import PaymentMethodsRequest
		return PaymentMethodsRequest(self.request_adapter, path_parameters)

	def payment_terms(self,
		company_id: UUID,
	) -> PaymentTermsRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .payment_terms import PaymentTermsRequest
		return PaymentTermsRequest(self.request_adapter, path_parameters)

	def picture(self,
		company_id: UUID,
	) -> PictureRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .picture import PictureRequest
		return PictureRequest(self.request_adapter, path_parameters)

	def purchase_invoice_lines(self,
		company_id: UUID,
	) -> PurchaseInvoiceLinesRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .purchase_invoice_lines import PurchaseInvoiceLinesRequest
		return PurchaseInvoiceLinesRequest(self.request_adapter, path_parameters)

	def purchase_invoices(self,
		company_id: UUID,
	) -> PurchaseInvoicesRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .purchase_invoices import PurchaseInvoicesRequest
		return PurchaseInvoicesRequest(self.request_adapter, path_parameters)

	def sales_credit_memo_lines(self,
		company_id: UUID,
	) -> SalesCreditMemoLinesRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .sales_credit_memo_lines import SalesCreditMemoLinesRequest
		return SalesCreditMemoLinesRequest(self.request_adapter, path_parameters)

	def sales_credit_memos(self,
		company_id: UUID,
	) -> SalesCreditMemosRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .sales_credit_memos import SalesCreditMemosRequest
		return SalesCreditMemosRequest(self.request_adapter, path_parameters)

	def sales_invoice_lines(self,
		company_id: UUID,
	) -> SalesInvoiceLinesRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .sales_invoice_lines import SalesInvoiceLinesRequest
		return SalesInvoiceLinesRequest(self.request_adapter, path_parameters)

	def sales_invoices(self,
		company_id: UUID,
	) -> SalesInvoicesRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .sales_invoices import SalesInvoicesRequest
		return SalesInvoicesRequest(self.request_adapter, path_parameters)

	def sales_order_lines(self,
		company_id: UUID,
	) -> SalesOrderLinesRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .sales_order_lines import SalesOrderLinesRequest
		return SalesOrderLinesRequest(self.request_adapter, path_parameters)

	def sales_orders(self,
		company_id: UUID,
	) -> SalesOrdersRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .sales_orders import SalesOrdersRequest
		return SalesOrdersRequest(self.request_adapter, path_parameters)

	def sales_quote_lines(self,
		company_id: UUID,
	) -> SalesQuoteLinesRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .sales_quote_lines import SalesQuoteLinesRequest
		return SalesQuoteLinesRequest(self.request_adapter, path_parameters)

	def sales_quotes(self,
		company_id: UUID,
	) -> SalesQuotesRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .sales_quotes import SalesQuotesRequest
		return SalesQuotesRequest(self.request_adapter, path_parameters)

	def shipment_methods(self,
		company_id: UUID,
	) -> ShipmentMethodsRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .shipment_methods import ShipmentMethodsRequest
		return ShipmentMethodsRequest(self.request_adapter, path_parameters)

	def tax_areas(self,
		company_id: UUID,
	) -> TaxAreasRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .tax_areas import TaxAreasRequest
		return TaxAreasRequest(self.request_adapter, path_parameters)

	def tax_groups(self,
		company_id: UUID,
	) -> TaxGroupsRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .tax_groups import TaxGroupsRequest
		return TaxGroupsRequest(self.request_adapter, path_parameters)

	def units_of_measure(self,
		company_id: UUID,
	) -> UnitsOfMeasureRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .units_of_measure import UnitsOfMeasureRequest
		return UnitsOfMeasureRequest(self.request_adapter, path_parameters)

	def vendors(self,
		company_id: UUID,
	) -> VendorsRequest:
		if company_id is None:
			raise TypeError("company_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["company%2Did"] =  company_id

		from .vendors import VendorsRequest
		return VendorsRequest(self.request_adapter, path_parameters)

