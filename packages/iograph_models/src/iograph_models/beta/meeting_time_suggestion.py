from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class MeetingTimeSuggestion(BaseModel):
	attendeeAvailability: Optional[list[AttendeeAvailability]] = Field(alias="attendeeAvailability", default=None,)
	confidence: float | str | ReferenceNumeric
	locations: Optional[list[Annotated[Union[LocationConstraintItem],Field(discriminator="odata_type")]]] = Field(alias="locations", default=None,)
	meetingTimeSlot: Optional[TimeSlot] = Field(alias="meetingTimeSlot", default=None,)
	order: Optional[int] = Field(alias="order", default=None,)
	organizerAvailability: Optional[FreeBusyStatus | str] = Field(alias="organizerAvailability", default=None,)
	suggestionReason: Optional[str] = Field(alias="suggestionReason", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .attendee_availability import AttendeeAvailability
from .reference_numeric import ReferenceNumeric
from .location_constraint_item import LocationConstraintItem
from .time_slot import TimeSlot
from .free_busy_status import FreeBusyStatus

