from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class BookingsAvailabilityWindow(BaseModel):
	availabilityType: Optional[BookingsServiceAvailabilityType | str] = Field(alias="availabilityType", default=None,)
	businessHours: Optional[list[BookingWorkHours]] = Field(alias="businessHours", default=None,)
	odata_type: Literal["#microsoft.graph.bookingsAvailabilityWindow"] = Field(alias="@odata.type", default="#microsoft.graph.bookingsAvailabilityWindow")
	endDate: Optional[str] = Field(alias="endDate", default=None,)
	startDate: Optional[str] = Field(alias="startDate", default=None,)

from .bookings_service_availability_type import BookingsServiceAvailabilityType
from .booking_work_hours import BookingWorkHours
