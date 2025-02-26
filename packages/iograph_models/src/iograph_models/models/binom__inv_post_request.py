from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Binom__invPostRequest(BaseModel):
	trials: Optional[str] = Field(default=None,alias="trials",)
	probabilityS: Optional[str] = Field(default=None,alias="probabilityS",)
	alpha: Optional[str] = Field(default=None,alias="alpha",)


