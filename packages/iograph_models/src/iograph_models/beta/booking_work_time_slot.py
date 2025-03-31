from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BookingWorkTimeSlot(BaseModel):
	end: Optional[str] = Field(alias="end", default=None,)
	start: Optional[str] = Field(alias="start", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

