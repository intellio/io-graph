from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SalesCreditMemo(BaseModel):
	billingPostalAddress: Optional[PostalAddressType] = Field(alias="billingPostalAddress", default=None,)
	billToCustomerId: Optional[UUID] = Field(alias="billToCustomerId", default=None,)
	billToCustomerNumber: Optional[str] = Field(alias="billToCustomerNumber", default=None,)
	billToName: Optional[str] = Field(alias="billToName", default=None,)
	creditMemoDate: Optional[str] = Field(alias="creditMemoDate", default=None,)
	currencyCode: Optional[str] = Field(alias="currencyCode", default=None,)
	currencyId: Optional[UUID] = Field(alias="currencyId", default=None,)
	customerId: Optional[UUID] = Field(alias="customerId", default=None,)
	customerName: Optional[str] = Field(alias="customerName", default=None,)
	customerNumber: Optional[str] = Field(alias="customerNumber", default=None,)
	discountAmount: Optional[int] = Field(alias="discountAmount", default=None,)
	discountAppliedBeforeTax: Optional[bool] = Field(alias="discountAppliedBeforeTax", default=None,)
	dueDate: Optional[str] = Field(alias="dueDate", default=None,)
	email: Optional[str] = Field(alias="email", default=None,)
	externalDocumentNumber: Optional[str] = Field(alias="externalDocumentNumber", default=None,)
	id: Optional[UUID] = Field(alias="id", default=None,)
	invoiceId: Optional[UUID] = Field(alias="invoiceId", default=None,)
	invoiceNumber: Optional[str] = Field(alias="invoiceNumber", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	number: Optional[str] = Field(alias="number", default=None,)
	paymentTermsId: Optional[UUID] = Field(alias="paymentTermsId", default=None,)
	phoneNumber: Optional[str] = Field(alias="phoneNumber", default=None,)
	pricesIncludeTax: Optional[bool] = Field(alias="pricesIncludeTax", default=None,)
	salesperson: Optional[str] = Field(alias="salesperson", default=None,)
	sellingPostalAddress: Optional[PostalAddressType] = Field(alias="sellingPostalAddress", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	totalAmountExcludingTax: Optional[int] = Field(alias="totalAmountExcludingTax", default=None,)
	totalAmountIncludingTax: Optional[int] = Field(alias="totalAmountIncludingTax", default=None,)
	totalTaxAmount: Optional[int] = Field(alias="totalTaxAmount", default=None,)
	currency: Optional[Currency] = Field(alias="currency", default=None,)
	customer: Optional[Customer] = Field(alias="customer", default=None,)
	paymentTerm: Optional[PaymentTerm] = Field(alias="paymentTerm", default=None,)
	salesCreditMemoLines: Optional[list[SalesCreditMemoLine]] = Field(alias="salesCreditMemoLines", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .postal_address_type import PostalAddressType
from .currency import Currency
from .customer import Customer
from .payment_term import PaymentTerm
from .sales_credit_memo_line import SalesCreditMemoLine
