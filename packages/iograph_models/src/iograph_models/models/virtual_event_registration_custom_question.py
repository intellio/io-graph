from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VirtualEventRegistrationCustomQuestion(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isRequired: Optional[bool] = Field(default=None,alias="isRequired",)
	answerChoices: list[Optional[str]] = Field(alias="answerChoices",)
	answerInputType: Optional[VirtualEventRegistrationQuestionAnswerInputType] = Field(default=None,alias="answerInputType",)

from .virtual_event_registration_question_answer_input_type import VirtualEventRegistrationQuestionAnswerInputType

