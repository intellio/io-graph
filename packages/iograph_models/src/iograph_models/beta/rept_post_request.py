from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ReptPostRequest(BaseModel):
	text: Optional[str] = Field(alias="text", default=None,)
	numberTimes: Optional[str] = Field(alias="numberTimes", default=None,)

