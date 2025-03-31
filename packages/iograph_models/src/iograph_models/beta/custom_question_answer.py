from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CustomQuestionAnswer(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.customQuestionAnswer"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	questionId: Optional[str] = Field(alias="questionId", default=None,)
	value: Optional[str] = Field(alias="value", default=None,)

