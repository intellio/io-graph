from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BookingWorkTimeSlot(BaseModel):
	endTime: Optional[str] = Field(default=None,alias="endTime",)
	startTime: Optional[str] = Field(default=None,alias="startTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


