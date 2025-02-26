from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class QuotientPostRequest(BaseModel):
	numerator: Optional[str] = Field(default=None,alias="numerator",)
	denominator: Optional[str] = Field(default=None,alias="denominator",)


