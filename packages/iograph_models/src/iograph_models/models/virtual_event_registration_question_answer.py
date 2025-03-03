from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VirtualEventRegistrationQuestionAnswer(BaseModel):
	booleanValue: Optional[bool] = Field(default=None,alias="booleanValue",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	multiChoiceValues: Optional[list[str]] = Field(default=None,alias="multiChoiceValues",)
	questionId: Optional[str] = Field(default=None,alias="questionId",)
	value: Optional[str] = Field(default=None,alias="value",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


