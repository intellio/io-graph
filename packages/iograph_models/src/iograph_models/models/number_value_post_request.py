from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Number_valuePostRequest(BaseModel):
	text: Optional[str] = Field(default=None,alias="text",)
	decimalSeparator: Optional[str] = Field(default=None,alias="decimalSeparator",)
	groupSeparator: Optional[str] = Field(default=None,alias="groupSeparator",)


