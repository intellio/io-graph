from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Update_recording_statusPostRequest(BaseModel):
	status: Optional[RecordingStatus | str] = Field(alias="status",default=None,)
	clientContext: Optional[str] = Field(alias="clientContext",default=None,)

from .recording_status import RecordingStatus

