from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MeetingRegistration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	allowedRegistrant: Optional[MeetingAudience | str] = Field(alias="allowedRegistrant",default=None,)
	registrants: SerializeAsAny[Optional[list[MeetingRegistrantBase]]] = Field(alias="registrants",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime",default=None,)
	registrationPageViewCount: Optional[int] = Field(alias="registrationPageViewCount",default=None,)
	registrationPageWebUrl: Optional[str] = Field(alias="registrationPageWebUrl",default=None,)
	speakers: Optional[list[MeetingSpeaker]] = Field(alias="speakers",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	subject: Optional[str] = Field(alias="subject",default=None,)
	customQuestions: Optional[list[MeetingRegistrationQuestion]] = Field(alias="customQuestions",default=None,)

from .meeting_audience import MeetingAudience
from .meeting_registrant_base import MeetingRegistrantBase
from .meeting_speaker import MeetingSpeaker
from .meeting_registration_question import MeetingRegistrationQuestion

