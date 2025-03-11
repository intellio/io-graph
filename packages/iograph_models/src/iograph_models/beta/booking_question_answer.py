from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BookingQuestionAnswer(BaseModel):
	answer: Optional[str] = Field(alias="answer",default=None,)
	answerInputType: Optional[AnswerInputType | str] = Field(alias="answerInputType",default=None,)
	answerOptions: Optional[list[str]] = Field(alias="answerOptions",default=None,)
	isRequired: Optional[bool] = Field(alias="isRequired",default=None,)
	question: Optional[str] = Field(alias="question",default=None,)
	questionId: Optional[str] = Field(alias="questionId",default=None,)
	selectedOptions: Optional[list[str]] = Field(alias="selectedOptions",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .answer_input_type import AnswerInputType

