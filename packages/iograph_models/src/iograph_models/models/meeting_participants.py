from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MeetingParticipants(BaseModel):
	attendees: Optional[list[MeetingParticipantInfo]] = Field(default=None,alias="attendees",)
	organizer: Optional[MeetingParticipantInfo] = Field(default=None,alias="organizer",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .meeting_participant_info import MeetingParticipantInfo
from .meeting_participant_info import MeetingParticipantInfo

