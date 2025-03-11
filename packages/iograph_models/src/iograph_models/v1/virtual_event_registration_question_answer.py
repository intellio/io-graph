from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEventRegistrationQuestionAnswer(BaseModel):
	booleanValue: Optional[bool] = Field(alias="booleanValue",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	multiChoiceValues: Optional[list[str]] = Field(alias="multiChoiceValues",default=None,)
	questionId: Optional[str] = Field(alias="questionId",default=None,)
	value: Optional[str] = Field(alias="value",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


