from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MeetingTimeSuggestionsResult(BaseModel):
	emptySuggestionsReason: Optional[str] = Field(alias="emptySuggestionsReason", default=None,)
	meetingTimeSuggestions: Optional[list[MeetingTimeSuggestion]] = Field(alias="meetingTimeSuggestions", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .meeting_time_suggestion import MeetingTimeSuggestion

