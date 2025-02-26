from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ReptPostRequest(BaseModel):
	text: Optional[str] = Field(default=None,alias="text",)
	numberTimes: Optional[str] = Field(default=None,alias="numberTimes",)


