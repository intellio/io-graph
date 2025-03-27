from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SalesOrder(BaseModel):
	billingPostalAddress: Optional[PostalAddressType] = Field(alias="billingPostalAddress", default=None,)
	billToCustomerId: Optional[UUID] = Field(alias="billToCustomerId", default=None,)
	billToCustomerNumber: Optional[str] = Field(alias="billToCustomerNumber", default=None,)
	billToName: Optional[str] = Field(alias="billToName", default=None,)
	currencyCode: Optional[str] = Field(alias="currencyCode", default=None,)
	currencyId: Optional[UUID] = Field(alias="currencyId", default=None,)
	customerId: Optional[UUID] = Field(alias="customerId", default=None,)
	customerName: Optional[str] = Field(alias="customerName", default=None,)
	customerNumber: Optional[str] = Field(alias="customerNumber", default=None,)
	discountAmount: Optional[int] = Field(alias="discountAmount", default=None,)
	discountAppliedBeforeTax: Optional[bool] = Field(alias="discountAppliedBeforeTax", default=None,)
	email: Optional[str] = Field(alias="email", default=None,)
	externalDocumentNumber: Optional[str] = Field(alias="externalDocumentNumber", default=None,)
	fullyShipped: Optional[bool] = Field(alias="fullyShipped", default=None,)
	id: Optional[UUID] = Field(alias="id", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	number: Optional[str] = Field(alias="number", default=None,)
	orderDate: Optional[str] = Field(alias="orderDate", default=None,)
	partialShipping: Optional[bool] = Field(alias="partialShipping", default=None,)
	paymentTermsId: Optional[UUID] = Field(alias="paymentTermsId", default=None,)
	phoneNumber: Optional[str] = Field(alias="phoneNumber", default=None,)
	pricesIncludeTax: Optional[bool] = Field(alias="pricesIncludeTax", default=None,)
	requestedDeliveryDate: Optional[str] = Field(alias="requestedDeliveryDate", default=None,)
	salesperson: Optional[str] = Field(alias="salesperson", default=None,)
	sellingPostalAddress: Optional[PostalAddressType] = Field(alias="sellingPostalAddress", default=None,)
	shippingPostalAddress: Optional[PostalAddressType] = Field(alias="shippingPostalAddress", default=None,)
	shipToContact: Optional[str] = Field(alias="shipToContact", default=None,)
	shipToName: Optional[str] = Field(alias="shipToName", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	totalAmountExcludingTax: Optional[int] = Field(alias="totalAmountExcludingTax", default=None,)
	totalAmountIncludingTax: Optional[int] = Field(alias="totalAmountIncludingTax", default=None,)
	totalTaxAmount: Optional[int] = Field(alias="totalTaxAmount", default=None,)
	currency: Optional[Currency] = Field(alias="currency", default=None,)
	customer: Optional[Customer] = Field(alias="customer", default=None,)
	paymentTerm: Optional[PaymentTerm] = Field(alias="paymentTerm", default=None,)
	salesOrderLines: Optional[list[SalesOrderLine]] = Field(alias="salesOrderLines", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .postal_address_type import PostalAddressType
from .postal_address_type import PostalAddressType
from .postal_address_type import PostalAddressType
from .currency import Currency
from .customer import Customer
from .payment_term import PaymentTerm
from .sales_order_line import SalesOrderLine

