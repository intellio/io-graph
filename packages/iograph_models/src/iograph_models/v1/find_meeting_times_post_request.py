from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Find_meeting_timesPostRequest(BaseModel):
	attendees: Optional[list[Annotated[Union[Attendee],Field(discriminator="odata_type")]]] = Field(alias="attendees", default=None,)
	locationConstraint: Optional[LocationConstraint] = Field(alias="locationConstraint", default=None,)
	timeConstraint: Optional[TimeConstraint] = Field(alias="timeConstraint", default=None,)
	meetingDuration: Optional[str] = Field(alias="meetingDuration", default=None,)
	maxCandidates: Optional[int] = Field(alias="maxCandidates", default=None,)
	isOrganizerOptional: Optional[bool] = Field(alias="isOrganizerOptional", default=None,)
	returnSuggestionReasons: Optional[bool] = Field(alias="returnSuggestionReasons", default=None,)
	minimumAttendeePercentage: float | str | ReferenceNumeric

from .attendee import Attendee
from .location_constraint import LocationConstraint
from .time_constraint import TimeConstraint
from .reference_numeric import ReferenceNumeric

