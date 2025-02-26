from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class VirtualEventRegistration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	cancelationDateTime: Optional[datetime] = Field(default=None,alias="cancelationDateTime",)
	email: Optional[str] = Field(default=None,alias="email",)
	externalRegistrationInformation: Optional[VirtualEventExternalRegistrationInformation] = Field(default=None,alias="externalRegistrationInformation",)
	firstName: Optional[str] = Field(default=None,alias="firstName",)
	lastName: Optional[str] = Field(default=None,alias="lastName",)
	preferredLanguage: Optional[str] = Field(default=None,alias="preferredLanguage",)
	preferredTimezone: Optional[str] = Field(default=None,alias="preferredTimezone",)
	registrationDateTime: Optional[datetime] = Field(default=None,alias="registrationDateTime",)
	registrationQuestionAnswers: list[VirtualEventRegistrationQuestionAnswer] = Field(alias="registrationQuestionAnswers",)
	status: Optional[VirtualEventAttendeeRegistrationStatus] = Field(default=None,alias="status",)
	userId: Optional[str] = Field(default=None,alias="userId",)
	sessions: list[VirtualEventSession] = Field(alias="sessions",)

from .virtual_event_external_registration_information import VirtualEventExternalRegistrationInformation
from .virtual_event_registration_question_answer import VirtualEventRegistrationQuestionAnswer
from .virtual_event_attendee_registration_status import VirtualEventAttendeeRegistrationStatus
from .virtual_event_session import VirtualEventSession

