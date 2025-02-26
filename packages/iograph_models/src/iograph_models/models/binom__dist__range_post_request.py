from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Binom__dist__rangePostRequest(BaseModel):
	trials: Optional[str] = Field(default=None,alias="trials",)
	probabilityS: Optional[str] = Field(default=None,alias="probabilityS",)
	numberS: Optional[str] = Field(default=None,alias="numberS",)
	numberS2: Optional[str] = Field(default=None,alias="numberS2",)


