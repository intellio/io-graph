from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Find_meeting_timesPostRequest(BaseModel):
	attendees: SerializeAsAny[Optional[list[AttendeeBase]]] = Field(default=None,alias="attendees",)
	locationConstraint: Optional[LocationConstraint] = Field(default=None,alias="locationConstraint",)
	timeConstraint: Optional[TimeConstraint] = Field(default=None,alias="timeConstraint",)
	meetingDuration: Optional[str] = Field(default=None,alias="meetingDuration",)
	maxCandidates: Optional[int] = Field(default=None,alias="maxCandidates",)
	isOrganizerOptional: Optional[bool] = Field(default=None,alias="isOrganizerOptional",)
	returnSuggestionReasons: Optional[bool] = Field(default=None,alias="returnSuggestionReasons",)
	minimumAttendeePercentage: float | str | ReferenceNumeric

from .attendee_base import AttendeeBase
from .location_constraint import LocationConstraint
from .time_constraint import TimeConstraint
from .reference_numeric import ReferenceNumeric

