from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MeetingTimeSuggestion(BaseModel):
	attendeeAvailability: Optional[list[AttendeeAvailability]] = Field(default=None,alias="attendeeAvailability",)
	confidence: float | str | ReferenceNumeric
	locations: Optional[list[Location]] = Field(default=None,alias="locations",)
	meetingTimeSlot: Optional[TimeSlot] = Field(default=None,alias="meetingTimeSlot",)
	order: Optional[int] = Field(default=None,alias="order",)
	organizerAvailability: Optional[FreeBusyStatus] = Field(default=None,alias="organizerAvailability",)
	suggestionReason: Optional[str] = Field(default=None,alias="suggestionReason",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .attendee_availability import AttendeeAvailability
from .reference_numeric import ReferenceNumeric
from .location import Location
from .time_slot import TimeSlot
from .free_busy_status import FreeBusyStatus

