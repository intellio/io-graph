from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Find_meeting_timesPostRequest(BaseModel):
	attendees: SerializeAsAny[Optional[list[AttendeeBase]]] = Field(alias="attendees",default=None,)
	locationConstraint: Optional[LocationConstraint] = Field(alias="locationConstraint",default=None,)
	timeConstraint: Optional[TimeConstraint] = Field(alias="timeConstraint",default=None,)
	meetingDuration: Optional[str] = Field(alias="meetingDuration",default=None,)
	maxCandidates: Optional[int] = Field(alias="maxCandidates",default=None,)
	isOrganizerOptional: Optional[bool] = Field(alias="isOrganizerOptional",default=None,)
	returnSuggestionReasons: Optional[bool] = Field(alias="returnSuggestionReasons",default=None,)
	minimumAttendeePercentage: float | str | ReferenceNumeric

from .attendee_base import AttendeeBase
from .location_constraint import LocationConstraint
from .time_constraint import TimeConstraint
from .reference_numeric import ReferenceNumeric

