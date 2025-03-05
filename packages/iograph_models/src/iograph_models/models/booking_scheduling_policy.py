from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BookingSchedulingPolicy(BaseModel):
	allowStaffSelection: Optional[bool] = Field(default=None,alias="allowStaffSelection",)
	customAvailabilities: Optional[list[BookingsAvailabilityWindow]] = Field(default=None,alias="customAvailabilities",)
	generalAvailability: SerializeAsAny[Optional[BookingsAvailability]] = Field(default=None,alias="generalAvailability",)
	isMeetingInviteToCustomersEnabled: Optional[bool] = Field(default=None,alias="isMeetingInviteToCustomersEnabled",)
	maximumAdvance: Optional[str] = Field(default=None,alias="maximumAdvance",)
	minimumLeadTime: Optional[str] = Field(default=None,alias="minimumLeadTime",)
	sendConfirmationsToOwner: Optional[bool] = Field(default=None,alias="sendConfirmationsToOwner",)
	timeSlotInterval: Optional[str] = Field(default=None,alias="timeSlotInterval",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .bookings_availability_window import BookingsAvailabilityWindow
from .bookings_availability import BookingsAvailability

