from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class BookingCustomQuestion(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.bookingCustomQuestion"] = Field(alias="@odata.type", default="#microsoft.graph.bookingCustomQuestion")
	answerInputType: Optional[AnswerInputType | str] = Field(alias="answerInputType", default=None,)
	answerOptions: Optional[list[str]] = Field(alias="answerOptions", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)

from .answer_input_type import AnswerInputType
