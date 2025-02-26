from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BookingWorkHours(BaseModel):
	day: Optional[DayOfWeek] = Field(default=None,alias="day",)
	timeSlots: list[BookingWorkTimeSlot] = Field(alias="timeSlots",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .day_of_week import DayOfWeek
from .booking_work_time_slot import BookingWorkTimeSlot

