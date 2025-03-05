from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEventWebinarRegistrationConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	capacity: Optional[int] = Field(default=None,alias="capacity",)
	registrationWebUrl: Optional[str] = Field(default=None,alias="registrationWebUrl",)
	questions: SerializeAsAny[Optional[list[VirtualEventRegistrationQuestionBase]]] = Field(default=None,alias="questions",)
	isManualApprovalEnabled: Optional[bool] = Field(default=None,alias="isManualApprovalEnabled",)
	isWaitlistEnabled: Optional[bool] = Field(default=None,alias="isWaitlistEnabled",)

from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase

