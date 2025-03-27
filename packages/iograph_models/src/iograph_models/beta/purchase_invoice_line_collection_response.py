from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PurchaseInvoiceLineCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PurchaseInvoiceLine]] = Field(alias="value", default=None,)

from .purchase_invoice_line import PurchaseInvoiceLine

