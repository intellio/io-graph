from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Round_upPostRequest(BaseModel):
	number: Optional[str] = Field(alias="number", default=None,)
	numDigits: Optional[str] = Field(alias="numDigits", default=None,)

