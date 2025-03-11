from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEventWebinarRegistrationConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	capacity: Optional[int] = Field(alias="capacity",default=None,)
	registrationWebUrl: Optional[str] = Field(alias="registrationWebUrl",default=None,)
	questions: SerializeAsAny[Optional[list[VirtualEventRegistrationQuestionBase]]] = Field(alias="questions",default=None,)
	isManualApprovalEnabled: Optional[bool] = Field(alias="isManualApprovalEnabled",default=None,)
	isWaitlistEnabled: Optional[bool] = Field(alias="isWaitlistEnabled",default=None,)

from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase

