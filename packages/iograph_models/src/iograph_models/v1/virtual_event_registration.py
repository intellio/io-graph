from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class VirtualEventRegistration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.virtualEventRegistration"] = Field(alias="@odata.type", default="#microsoft.graph.virtualEventRegistration")
	cancelationDateTime: Optional[datetime] = Field(alias="cancelationDateTime", default=None,)
	email: Optional[str] = Field(alias="email", default=None,)
	externalRegistrationInformation: Optional[VirtualEventExternalRegistrationInformation] = Field(alias="externalRegistrationInformation", default=None,)
	firstName: Optional[str] = Field(alias="firstName", default=None,)
	lastName: Optional[str] = Field(alias="lastName", default=None,)
	preferredLanguage: Optional[str] = Field(alias="preferredLanguage", default=None,)
	preferredTimezone: Optional[str] = Field(alias="preferredTimezone", default=None,)
	registrationDateTime: Optional[datetime] = Field(alias="registrationDateTime", default=None,)
	registrationQuestionAnswers: Optional[list[VirtualEventRegistrationQuestionAnswer]] = Field(alias="registrationQuestionAnswers", default=None,)
	status: Optional[VirtualEventAttendeeRegistrationStatus | str] = Field(alias="status", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	sessions: Optional[list[VirtualEventSession]] = Field(alias="sessions", default=None,)

from .virtual_event_external_registration_information import VirtualEventExternalRegistrationInformation
from .virtual_event_registration_question_answer import VirtualEventRegistrationQuestionAnswer
from .virtual_event_attendee_registration_status import VirtualEventAttendeeRegistrationStatus
from .virtual_event_session import VirtualEventSession
