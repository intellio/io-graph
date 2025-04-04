from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MatchedCondition(BaseModel):
	condition: Optional[str] = Field(alias="condition", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	values: Optional[list[str]] = Field(alias="values", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

