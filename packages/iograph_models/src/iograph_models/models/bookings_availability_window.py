from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BookingsAvailabilityWindow(BaseModel):
	availabilityType: Optional[str | BookingsServiceAvailabilityType] = Field(alias="availabilityType",default=None,)
	businessHours: Optional[list[BookingWorkHours]] = Field(alias="businessHours",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	endDate: Optional[str] = Field(alias="endDate",default=None,)
	startDate: Optional[str] = Field(alias="startDate",default=None,)

from .bookings_service_availability_type import BookingsServiceAvailabilityType
from .booking_work_hours import BookingWorkHours

