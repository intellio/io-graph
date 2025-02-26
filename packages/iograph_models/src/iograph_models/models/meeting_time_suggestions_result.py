from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MeetingTimeSuggestionsResult(BaseModel):
	emptySuggestionsReason: Optional[str] = Field(default=None,alias="emptySuggestionsReason",)
	meetingTimeSuggestions: list[MeetingTimeSuggestion] = Field(alias="meetingTimeSuggestions",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .meeting_time_suggestion import MeetingTimeSuggestion

