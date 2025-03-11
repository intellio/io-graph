from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CallRecordsCallRecord(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime",default=None,)
	joinWebUrl: Optional[str] = Field(alias="joinWebUrl",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	modalities: Optional[list[CallRecordsModality | str]] = Field(alias="modalities",default=None,)
	organizer: SerializeAsAny[Optional[IdentitySet]] = Field(alias="organizer",default=None,)
	participants: SerializeAsAny[Optional[list[IdentitySet]]] = Field(alias="participants",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	type: Optional[CallRecordsCallType | str] = Field(alias="type",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)
	organizer_v2: Optional[CallRecordsOrganizer] = Field(alias="organizer_v2",default=None,)
	participants_v2: Optional[list[CallRecordsParticipant]] = Field(alias="participants_v2",default=None,)
	sessions: Optional[list[CallRecordsSession]] = Field(alias="sessions",default=None,)

from .call_records_modality import CallRecordsModality
from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .call_records_call_type import CallRecordsCallType
from .call_records_organizer import CallRecordsOrganizer
from .call_records_participant import CallRecordsParticipant
from .call_records_session import CallRecordsSession

