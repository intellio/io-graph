from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Binom__distPostRequest(BaseModel):
	numberS: Optional[str] = Field(default=None,alias="numberS",)
	trials: Optional[str] = Field(default=None,alias="trials",)
	probabilityS: Optional[str] = Field(default=None,alias="probabilityS",)
	cumulative: Optional[str] = Field(default=None,alias="cumulative",)


