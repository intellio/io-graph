from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallTranscriptEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	callId: Optional[str] = Field(alias="callId",default=None,)
	callTranscriptICalUid: Optional[str] = Field(alias="callTranscriptICalUid",default=None,)
	meetingOrganizer: SerializeAsAny[Optional[IdentitySet]] = Field(alias="meetingOrganizer",default=None,)

from .identity_set import IdentitySet

