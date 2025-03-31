from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TimePostRequest(BaseModel):
	hour: Optional[str] = Field(alias="hour", default=None,)
	minute: Optional[str] = Field(alias="minute", default=None,)
	second: Optional[str] = Field(alias="second", default=None,)

