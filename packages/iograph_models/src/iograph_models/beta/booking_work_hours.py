from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BookingWorkHours(BaseModel):
	day: Optional[DayOfWeek | str] = Field(alias="day", default=None,)
	timeSlots: Optional[list[BookingWorkTimeSlot]] = Field(alias="timeSlots", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .day_of_week import DayOfWeek
from .booking_work_time_slot import BookingWorkTimeSlot

