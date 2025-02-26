from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MeetingTimeSuggestionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[MeetingTimeSuggestion] = Field(alias="value",)

from .meeting_time_suggestion import MeetingTimeSuggestion

