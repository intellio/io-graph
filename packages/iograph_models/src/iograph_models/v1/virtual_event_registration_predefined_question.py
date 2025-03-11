from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEventRegistrationPredefinedQuestion(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isRequired: Optional[bool] = Field(alias="isRequired",default=None,)
	label: Optional[VirtualEventRegistrationPredefinedQuestionLabel | str] = Field(alias="label",default=None,)

from .virtual_event_registration_predefined_question_label import VirtualEventRegistrationPredefinedQuestionLabel

