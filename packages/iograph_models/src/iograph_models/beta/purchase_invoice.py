from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PurchaseInvoice(BaseModel):
	buyFromAddress: Optional[PostalAddressType] = Field(alias="buyFromAddress", default=None,)
	currencyCode: Optional[str] = Field(alias="currencyCode", default=None,)
	currencyId: Optional[UUID] = Field(alias="currencyId", default=None,)
	discountAmount: Optional[int] = Field(alias="discountAmount", default=None,)
	discountAppliedBeforeTax: Optional[bool] = Field(alias="discountAppliedBeforeTax", default=None,)
	dueDate: Optional[str] = Field(alias="dueDate", default=None,)
	id: Optional[UUID] = Field(alias="id", default=None,)
	invoiceDate: Optional[str] = Field(alias="invoiceDate", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	number: Optional[str] = Field(alias="number", default=None,)
	payToAddress: Optional[PostalAddressType] = Field(alias="payToAddress", default=None,)
	payToContact: Optional[str] = Field(alias="payToContact", default=None,)
	payToName: Optional[str] = Field(alias="payToName", default=None,)
	payToVendorId: Optional[UUID] = Field(alias="payToVendorId", default=None,)
	payToVendorNumber: Optional[str] = Field(alias="payToVendorNumber", default=None,)
	pricesIncludeTax: Optional[bool] = Field(alias="pricesIncludeTax", default=None,)
	shipToAddress: Optional[PostalAddressType] = Field(alias="shipToAddress", default=None,)
	shipToContact: Optional[str] = Field(alias="shipToContact", default=None,)
	shipToName: Optional[str] = Field(alias="shipToName", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	totalAmountExcludingTax: Optional[int] = Field(alias="totalAmountExcludingTax", default=None,)
	totalAmountIncludingTax: Optional[int] = Field(alias="totalAmountIncludingTax", default=None,)
	totalTaxAmount: Optional[int] = Field(alias="totalTaxAmount", default=None,)
	vendorId: Optional[UUID] = Field(alias="vendorId", default=None,)
	vendorInvoiceNumber: Optional[str] = Field(alias="vendorInvoiceNumber", default=None,)
	vendorName: Optional[str] = Field(alias="vendorName", default=None,)
	vendorNumber: Optional[str] = Field(alias="vendorNumber", default=None,)
	currency: Optional[Currency] = Field(alias="currency", default=None,)
	purchaseInvoiceLines: Optional[list[PurchaseInvoiceLine]] = Field(alias="purchaseInvoiceLines", default=None,)
	vendor: Optional[Vendor] = Field(alias="vendor", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .postal_address_type import PostalAddressType
from .currency import Currency
from .purchase_invoice_line import PurchaseInvoiceLine
from .vendor import Vendor
