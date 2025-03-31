from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MeetingTimeSuggestionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MeetingTimeSuggestion]] = Field(alias="value", default=None,)

from .meeting_time_suggestion import MeetingTimeSuggestion
