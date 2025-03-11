from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CallTranscript(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	callId: Optional[str] = Field(alias="callId",default=None,)
	content: Optional[str] = Field(alias="content",default=None,)
	contentCorrelationId: Optional[str] = Field(alias="contentCorrelationId",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime",default=None,)
	meetingId: Optional[str] = Field(alias="meetingId",default=None,)
	meetingOrganizer: SerializeAsAny[Optional[IdentitySet]] = Field(alias="meetingOrganizer",default=None,)
	metadataContent: Optional[str] = Field(alias="metadataContent",default=None,)
	transcriptContentUrl: Optional[str] = Field(alias="transcriptContentUrl",default=None,)

from .identity_set import IdentitySet

