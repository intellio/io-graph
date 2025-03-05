from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class BookingCustomer(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	addresses: Optional[list[PhysicalAddress]] = Field(default=None,alias="addresses",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	emailAddress: Optional[str] = Field(default=None,alias="emailAddress",)
	lastUpdatedDateTime: Optional[datetime] = Field(default=None,alias="lastUpdatedDateTime",)
	phones: Optional[list[Phone]] = Field(default=None,alias="phones",)

from .physical_address import PhysicalAddress
from .phone import Phone

