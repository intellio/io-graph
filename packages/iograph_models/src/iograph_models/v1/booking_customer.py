from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class BookingCustomer(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.bookingCustomer"] = Field(alias="@odata.type", default="#microsoft.graph.bookingCustomer")
	addresses: Optional[list[PhysicalAddress]] = Field(alias="addresses", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	emailAddress: Optional[str] = Field(alias="emailAddress", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	phones: Optional[list[Phone]] = Field(alias="phones", default=None,)

from .physical_address import PhysicalAddress
from .phone import Phone

