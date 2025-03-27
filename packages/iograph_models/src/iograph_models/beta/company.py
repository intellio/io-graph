from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Company(BaseModel):
	businessProfileId: Optional[str] = Field(alias="businessProfileId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[UUID] = Field(alias="id", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	systemVersion: Optional[str] = Field(alias="systemVersion", default=None,)
	accounts: Optional[list[Account]] = Field(alias="accounts", default=None,)
	agedAccountsPayable: Optional[list[AgedAccountsPayable]] = Field(alias="agedAccountsPayable", default=None,)
	agedAccountsReceivable: Optional[list[AgedAccountsReceivable]] = Field(alias="agedAccountsReceivable", default=None,)
	companyInformation: Optional[list[CompanyInformation]] = Field(alias="companyInformation", default=None,)
	countriesRegions: Optional[list[CountryRegion]] = Field(alias="countriesRegions", default=None,)
	currencies: Optional[list[Currency]] = Field(alias="currencies", default=None,)
	customerPaymentJournals: Optional[list[CustomerPaymentJournal]] = Field(alias="customerPaymentJournals", default=None,)
	customerPayments: Optional[list[CustomerPayment]] = Field(alias="customerPayments", default=None,)
	customers: Optional[list[Customer]] = Field(alias="customers", default=None,)
	dimensions: Optional[list[Dimension]] = Field(alias="dimensions", default=None,)
	dimensionValues: Optional[list[DimensionValue]] = Field(alias="dimensionValues", default=None,)
	employees: Optional[list[Employee]] = Field(alias="employees", default=None,)
	generalLedgerEntries: Optional[list[GeneralLedgerEntry]] = Field(alias="generalLedgerEntries", default=None,)
	itemCategories: Optional[list[ItemCategory]] = Field(alias="itemCategories", default=None,)
	items: Optional[list[Item]] = Field(alias="items", default=None,)
	journalLines: Optional[list[JournalLine]] = Field(alias="journalLines", default=None,)
	journals: Optional[list[Journal]] = Field(alias="journals", default=None,)
	paymentMethods: Optional[list[PaymentMethod]] = Field(alias="paymentMethods", default=None,)
	paymentTerms: Optional[list[PaymentTerm]] = Field(alias="paymentTerms", default=None,)
	picture: Optional[list[Picture]] = Field(alias="picture", default=None,)
	purchaseInvoiceLines: Optional[list[PurchaseInvoiceLine]] = Field(alias="purchaseInvoiceLines", default=None,)
	purchaseInvoices: Optional[list[PurchaseInvoice]] = Field(alias="purchaseInvoices", default=None,)
	salesCreditMemoLines: Optional[list[SalesCreditMemoLine]] = Field(alias="salesCreditMemoLines", default=None,)
	salesCreditMemos: Optional[list[SalesCreditMemo]] = Field(alias="salesCreditMemos", default=None,)
	salesInvoiceLines: Optional[list[SalesInvoiceLine]] = Field(alias="salesInvoiceLines", default=None,)
	salesInvoices: Optional[list[SalesInvoice]] = Field(alias="salesInvoices", default=None,)
	salesOrderLines: Optional[list[SalesOrderLine]] = Field(alias="salesOrderLines", default=None,)
	salesOrders: Optional[list[SalesOrder]] = Field(alias="salesOrders", default=None,)
	salesQuoteLines: Optional[list[SalesQuoteLine]] = Field(alias="salesQuoteLines", default=None,)
	salesQuotes: Optional[list[SalesQuote]] = Field(alias="salesQuotes", default=None,)
	shipmentMethods: Optional[list[ShipmentMethod]] = Field(alias="shipmentMethods", default=None,)
	taxAreas: Optional[list[TaxArea]] = Field(alias="taxAreas", default=None,)
	taxGroups: Optional[list[TaxGroup]] = Field(alias="taxGroups", default=None,)
	unitsOfMeasure: Optional[list[UnitOfMeasure]] = Field(alias="unitsOfMeasure", default=None,)
	vendors: Optional[list[Vendor]] = Field(alias="vendors", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .account import Account
from .aged_accounts_payable import AgedAccountsPayable
from .aged_accounts_receivable import AgedAccountsReceivable
from .company_information import CompanyInformation
from .country_region import CountryRegion
from .currency import Currency
from .customer_payment_journal import CustomerPaymentJournal
from .customer_payment import CustomerPayment
from .customer import Customer
from .dimension import Dimension
from .dimension_value import DimensionValue
from .employee import Employee
from .general_ledger_entry import GeneralLedgerEntry
from .item_category import ItemCategory
from .item import Item
from .journal_line import JournalLine
from .journal import Journal
from .payment_method import PaymentMethod
from .payment_term import PaymentTerm
from .picture import Picture
from .purchase_invoice_line import PurchaseInvoiceLine
from .purchase_invoice import PurchaseInvoice
from .sales_credit_memo_line import SalesCreditMemoLine
from .sales_credit_memo import SalesCreditMemo
from .sales_invoice_line import SalesInvoiceLine
from .sales_invoice import SalesInvoice
from .sales_order_line import SalesOrderLine
from .sales_order import SalesOrder
from .sales_quote_line import SalesQuoteLine
from .sales_quote import SalesQuote
from .shipment_method import ShipmentMethod
from .tax_area import TaxArea
from .tax_group import TaxGroup
from .unit_of_measure import UnitOfMeasure
from .vendor import Vendor

