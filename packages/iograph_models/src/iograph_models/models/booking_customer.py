from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class BookingCustomer(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	addresses: list[PhysicalAddress] = Field(alias="addresses",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	emailAddress: Optional[str] = Field(default=None,alias="emailAddress",)
	lastUpdatedDateTime: Optional[datetime] = Field(default=None,alias="lastUpdatedDateTime",)
	phones: list[Phone] = Field(alias="phones",)

from .physical_address import PhysicalAddress
from .phone import Phone

