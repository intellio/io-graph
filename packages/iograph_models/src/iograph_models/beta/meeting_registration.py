from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class MeetingRegistration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.meetingRegistration"] = Field(alias="@odata.type", default="#microsoft.graph.meetingRegistration")
	allowedRegistrant: Optional[MeetingAudience | str] = Field(alias="allowedRegistrant", default=None,)
	registrants: Optional[list[Annotated[Union[ExternalMeetingRegistrant, MeetingRegistrant],Field(discriminator="odata_type")]]] = Field(alias="registrants", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	registrationPageViewCount: Optional[int] = Field(alias="registrationPageViewCount", default=None,)
	registrationPageWebUrl: Optional[str] = Field(alias="registrationPageWebUrl", default=None,)
	speakers: Optional[list[MeetingSpeaker]] = Field(alias="speakers", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	customQuestions: Optional[list[MeetingRegistrationQuestion]] = Field(alias="customQuestions", default=None,)

from .meeting_audience import MeetingAudience
from .external_meeting_registrant import ExternalMeetingRegistrant
from .meeting_registrant import MeetingRegistrant
from .meeting_speaker import MeetingSpeaker
from .meeting_registration_question import MeetingRegistrationQuestion
