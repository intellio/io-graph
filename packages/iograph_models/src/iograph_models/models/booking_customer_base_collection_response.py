from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BookingCustomerBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[BookingCustomerBase] = Field(alias="value",)

from .booking_customer_base import BookingCustomerBase

