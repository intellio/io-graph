from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BookingQuestionAssignment(BaseModel):
	isRequired: Optional[bool] = Field(alias="isRequired", default=None,)
	questionId: Optional[str] = Field(alias="questionId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

