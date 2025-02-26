from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallTranscriptEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	callId: Optional[str] = Field(default=None,alias="callId",)
	callTranscriptICalUid: Optional[str] = Field(default=None,alias="callTranscriptICalUid",)
	meetingOrganizer: Optional[IdentitySet] = Field(default=None,alias="meetingOrganizer",)

from .identity_set import IdentitySet

