from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEventRegistrationCustomQuestion(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.virtualEventRegistrationCustomQuestion"] = Field(alias="@odata.type", default="#microsoft.graph.virtualEventRegistrationCustomQuestion")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isRequired: Optional[bool] = Field(alias="isRequired", default=None,)
	answerChoices: Optional[list[str]] = Field(alias="answerChoices", default=None,)
	answerInputType: Optional[VirtualEventRegistrationQuestionAnswerInputType | str] = Field(alias="answerInputType", default=None,)

from .virtual_event_registration_question_answer_input_type import VirtualEventRegistrationQuestionAnswerInputType

