from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TimevaluePostRequest(BaseModel):
	timeText: Optional[str] = Field(alias="timeText", default=None,)

