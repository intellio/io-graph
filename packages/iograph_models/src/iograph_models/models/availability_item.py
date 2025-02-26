from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AvailabilityItem(BaseModel):
	endDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="endDateTime",)
	serviceId: Optional[str] = Field(default=None,alias="serviceId",)
	startDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="startDateTime",)
	status: Optional[BookingsAvailabilityStatus] = Field(default=None,alias="status",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone
from .bookings_availability_status import BookingsAvailabilityStatus

