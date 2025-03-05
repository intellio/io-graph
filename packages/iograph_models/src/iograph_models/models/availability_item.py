from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AvailabilityItem(BaseModel):
	endDateTime: Optional[DateTimeTimeZone] = Field(alias="endDateTime",default=None,)
	serviceId: Optional[str] = Field(alias="serviceId",default=None,)
	startDateTime: Optional[DateTimeTimeZone] = Field(alias="startDateTime",default=None,)
	status: Optional[str | BookingsAvailabilityStatus] = Field(alias="status",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone
from .bookings_availability_status import BookingsAvailabilityStatus

