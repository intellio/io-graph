from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SalesOrderLine(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.salesOrderLine"] = Field(alias="@odata.type", default="#microsoft.graph.salesOrderLine")
	accountId: Optional[UUID] = Field(alias="accountId", default=None,)
	amountExcludingTax: Optional[int] = Field(alias="amountExcludingTax", default=None,)
	amountIncludingTax: Optional[int] = Field(alias="amountIncludingTax", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	discountAmount: Optional[int] = Field(alias="discountAmount", default=None,)
	discountAppliedBeforeTax: Optional[bool] = Field(alias="discountAppliedBeforeTax", default=None,)
	discountPercent: Optional[int] = Field(alias="discountPercent", default=None,)
	documentId: Optional[UUID] = Field(alias="documentId", default=None,)
	invoiceDiscountAllocation: Optional[int] = Field(alias="invoiceDiscountAllocation", default=None,)
	invoicedQuantity: Optional[int] = Field(alias="invoicedQuantity", default=None,)
	invoiceQuantity: Optional[int] = Field(alias="invoiceQuantity", default=None,)
	itemId: Optional[UUID] = Field(alias="itemId", default=None,)
	lineType: Optional[str] = Field(alias="lineType", default=None,)
	netAmount: Optional[int] = Field(alias="netAmount", default=None,)
	netAmountIncludingTax: Optional[int] = Field(alias="netAmountIncludingTax", default=None,)
	netTaxAmount: Optional[int] = Field(alias="netTaxAmount", default=None,)
	quantity: Optional[int] = Field(alias="quantity", default=None,)
	sequence: Optional[int] = Field(alias="sequence", default=None,)
	shipmentDate: Optional[str] = Field(alias="shipmentDate", default=None,)
	shippedQuantity: Optional[int] = Field(alias="shippedQuantity", default=None,)
	shipQuantity: Optional[int] = Field(alias="shipQuantity", default=None,)
	taxCode: Optional[str] = Field(alias="taxCode", default=None,)
	taxPercent: Optional[int] = Field(alias="taxPercent", default=None,)
	totalTaxAmount: Optional[int] = Field(alias="totalTaxAmount", default=None,)
	unitOfMeasureId: Optional[UUID] = Field(alias="unitOfMeasureId", default=None,)
	unitPrice: Optional[int] = Field(alias="unitPrice", default=None,)
	account: Optional[Account] = Field(alias="account", default=None,)
	item: Optional[Item] = Field(alias="item", default=None,)

from .account import Account
from .item import Item
