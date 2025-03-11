from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordingEventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	callId: Optional[str] = Field(alias="callId",default=None,)
	callRecordingDisplayName: Optional[str] = Field(alias="callRecordingDisplayName",default=None,)
	callRecordingDuration: Optional[str] = Field(alias="callRecordingDuration",default=None,)
	callRecordingStatus: Optional[CallRecordingStatus | str] = Field(alias="callRecordingStatus",default=None,)
	callRecordingUrl: Optional[str] = Field(alias="callRecordingUrl",default=None,)
	initiator: SerializeAsAny[Optional[IdentitySet]] = Field(alias="initiator",default=None,)
	meetingOrganizer: SerializeAsAny[Optional[IdentitySet]] = Field(alias="meetingOrganizer",default=None,)

from .call_recording_status import CallRecordingStatus
from .identity_set import IdentitySet
from .identity_set import IdentitySet

