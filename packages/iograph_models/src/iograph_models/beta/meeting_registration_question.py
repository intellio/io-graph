from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MeetingRegistrationQuestion(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	answerInputType: Optional[AnswerInputType | str] = Field(alias="answerInputType",default=None,)
	answerOptions: Optional[list[str]] = Field(alias="answerOptions",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isRequired: Optional[bool] = Field(alias="isRequired",default=None,)

from .answer_input_type import AnswerInputType

