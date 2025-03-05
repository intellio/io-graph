from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MeetingParticipants(BaseModel):
	attendees: SerializeAsAny[Optional[list[MeetingParticipantInfo]]] = Field(alias="attendees",default=None,)
	organizer: SerializeAsAny[Optional[MeetingParticipantInfo]] = Field(alias="organizer",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .meeting_participant_info import MeetingParticipantInfo
from .meeting_participant_info import MeetingParticipantInfo

