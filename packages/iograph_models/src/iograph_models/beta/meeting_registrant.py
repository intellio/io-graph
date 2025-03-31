from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MeetingRegistrant(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.meetingRegistrant"] = Field(alias="@odata.type", default="#microsoft.graph.meetingRegistrant")
	joinWebUrl: Optional[str] = Field(alias="joinWebUrl", default=None,)
	customQuestionAnswers: Optional[list[CustomQuestionAnswer]] = Field(alias="customQuestionAnswers", default=None,)
	email: Optional[str] = Field(alias="email", default=None,)
	firstName: Optional[str] = Field(alias="firstName", default=None,)
	lastName: Optional[str] = Field(alias="lastName", default=None,)
	registrationDateTime: Optional[datetime] = Field(alias="registrationDateTime", default=None,)
	status: Optional[MeetingRegistrantStatus | str] = Field(alias="status", default=None,)

from .custom_question_answer import CustomQuestionAnswer
from .meeting_registrant_status import MeetingRegistrantStatus
