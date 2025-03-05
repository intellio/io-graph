from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEventRegistrationPredefinedQuestion(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isRequired: Optional[bool] = Field(default=None,alias="isRequired",)
	label: Optional[VirtualEventRegistrationPredefinedQuestionLabel] = Field(default=None,alias="label",)

from .virtual_event_registration_predefined_question_label import VirtualEventRegistrationPredefinedQuestionLabel

