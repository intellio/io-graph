from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BitxorPostRequest(BaseModel):
	number1: Optional[str] = Field(alias="number1", default=None,)
	number2: Optional[str] = Field(alias="number2", default=None,)

