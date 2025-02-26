from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BookingQuestionAssignment(BaseModel):
	isRequired: Optional[bool] = Field(default=None,alias="isRequired",)
	questionId: Optional[str] = Field(default=None,alias="questionId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


