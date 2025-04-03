from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MeetingRegistrationQuestion(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.meetingRegistrationQuestion"] = Field(alias="@odata.type", default="#microsoft.graph.meetingRegistrationQuestion")
	answerInputType: Optional[AnswerInputType | str] = Field(alias="answerInputType", default=None,)
	answerOptions: Optional[list[str]] = Field(alias="answerOptions", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isRequired: Optional[bool] = Field(alias="isRequired", default=None,)

from .answer_input_type import AnswerInputType
