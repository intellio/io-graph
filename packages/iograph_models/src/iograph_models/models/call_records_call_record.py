from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CallRecordsCallRecord(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	joinWebUrl: Optional[str] = Field(default=None,alias="joinWebUrl",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	modalities: Optional[list[CallRecordsModality]] = Field(default=None,alias="modalities",)
	organizer: Optional[IdentitySet] = Field(default=None,alias="organizer",)
	participants: Optional[list[IdentitySet]] = Field(default=None,alias="participants",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	type: Optional[CallRecordsCallType] = Field(default=None,alias="type",)
	version: Optional[int] = Field(default=None,alias="version",)
	organizer_v2: Optional[CallRecordsOrganizer] = Field(default=None,alias="organizer_v2",)
	participants_v2: Optional[list[CallRecordsParticipant]] = Field(default=None,alias="participants_v2",)
	sessions: Optional[list[CallRecordsSession]] = Field(default=None,alias="sessions",)

from .call_records_modality import CallRecordsModality
from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .call_records_call_type import CallRecordsCallType
from .call_records_organizer import CallRecordsOrganizer
from .call_records_participant import CallRecordsParticipant
from .call_records_session import CallRecordsSession

