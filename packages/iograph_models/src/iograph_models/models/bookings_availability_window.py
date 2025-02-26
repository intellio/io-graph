from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BookingsAvailabilityWindow(BaseModel):
	availabilityType: Optional[BookingsServiceAvailabilityType] = Field(default=None,alias="availabilityType",)
	businessHours: list[BookingWorkHours] = Field(alias="businessHours",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	endDate: Optional[str] = Field(default=None,alias="endDate",)
	startDate: Optional[str] = Field(default=None,alias="startDate",)

from .bookings_service_availability_type import BookingsServiceAvailabilityType
from .booking_work_hours import BookingWorkHours

