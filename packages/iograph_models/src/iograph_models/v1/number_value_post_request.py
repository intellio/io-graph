from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Number_valuePostRequest(BaseModel):
	text: Optional[str] = Field(alias="text", default=None,)
	decimalSeparator: Optional[str] = Field(alias="decimalSeparator", default=None,)
	groupSeparator: Optional[str] = Field(alias="groupSeparator", default=None,)

