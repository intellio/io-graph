from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RecordingInfo(BaseModel):
	initiator: SerializeAsAny[Optional[IdentitySet]] = Field(alias="initiator",default=None,)
	recordingStatus: Optional[RecordingStatus | str] = Field(alias="recordingStatus",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_set import IdentitySet
from .recording_status import RecordingStatus

