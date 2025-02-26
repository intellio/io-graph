from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CallRecording(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	callId: Optional[str] = Field(default=None,alias="callId",)
	content: Optional[str] = Field(default=None,alias="content",)
	contentCorrelationId: Optional[str] = Field(default=None,alias="contentCorrelationId",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	meetingId: Optional[str] = Field(default=None,alias="meetingId",)
	meetingOrganizer: Optional[IdentitySet] = Field(default=None,alias="meetingOrganizer",)
	recordingContentUrl: Optional[str] = Field(default=None,alias="recordingContentUrl",)

from .identity_set import IdentitySet

