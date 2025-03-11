from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalMeetingRegistration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	allowedRegistrant: Optional[MeetingAudience | str] = Field(alias="allowedRegistrant",default=None,)
	registrants: SerializeAsAny[Optional[list[MeetingRegistrantBase]]] = Field(alias="registrants",default=None,)

from .meeting_audience import MeetingAudience
from .meeting_registrant_base import MeetingRegistrantBase

