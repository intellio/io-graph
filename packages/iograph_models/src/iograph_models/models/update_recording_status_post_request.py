from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Update_recording_statusPostRequest(BaseModel):
	status: Optional[RecordingStatus] = Field(default=None,alias="status",)
	clientContext: Optional[str] = Field(default=None,alias="clientContext",)

from .recording_status import RecordingStatus

