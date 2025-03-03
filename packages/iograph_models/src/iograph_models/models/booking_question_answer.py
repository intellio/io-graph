from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BookingQuestionAnswer(BaseModel):
	answer: Optional[str] = Field(default=None,alias="answer",)
	answerInputType: Optional[AnswerInputType] = Field(default=None,alias="answerInputType",)
	answerOptions: Optional[list[str]] = Field(default=None,alias="answerOptions",)
	isRequired: Optional[bool] = Field(default=None,alias="isRequired",)
	question: Optional[str] = Field(default=None,alias="question",)
	questionId: Optional[str] = Field(default=None,alias="questionId",)
	selectedOptions: Optional[list[str]] = Field(default=None,alias="selectedOptions",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .answer_input_type import AnswerInputType

