from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class BookingSchedulingPolicy(BaseModel):
	allowStaffSelection: Optional[bool] = Field(alias="allowStaffSelection", default=None,)
	customAvailabilities: Optional[list[BookingsAvailabilityWindow]] = Field(alias="customAvailabilities", default=None,)
	generalAvailability: Optional[Union[BookingsAvailabilityWindow]] = Field(alias="generalAvailability", default=None,discriminator="odata_type", )
	isMeetingInviteToCustomersEnabled: Optional[bool] = Field(alias="isMeetingInviteToCustomersEnabled", default=None,)
	maximumAdvance: Optional[str] = Field(alias="maximumAdvance", default=None,)
	minimumLeadTime: Optional[str] = Field(alias="minimumLeadTime", default=None,)
	sendConfirmationsToOwner: Optional[bool] = Field(alias="sendConfirmationsToOwner", default=None,)
	timeSlotInterval: Optional[str] = Field(alias="timeSlotInterval", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .bookings_availability_window import BookingsAvailabilityWindow
