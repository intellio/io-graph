from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallRecordingEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	callId: Optional[str] = Field(default=None,alias="callId",)
	callRecordingDisplayName: Optional[str] = Field(default=None,alias="callRecordingDisplayName",)
	callRecordingDuration: Optional[str] = Field(default=None,alias="callRecordingDuration",)
	callRecordingStatus: Optional[CallRecordingStatus] = Field(default=None,alias="callRecordingStatus",)
	callRecordingUrl: Optional[str] = Field(default=None,alias="callRecordingUrl",)
	initiator: Optional[IdentitySet] = Field(default=None,alias="initiator",)
	meetingOrganizer: Optional[IdentitySet] = Field(default=None,alias="meetingOrganizer",)

from .call_recording_status import CallRecordingStatus
from .identity_set import IdentitySet
from .identity_set import IdentitySet

