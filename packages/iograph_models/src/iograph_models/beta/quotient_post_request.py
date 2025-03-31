from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class QuotientPostRequest(BaseModel):
	numerator: Optional[str] = Field(alias="numerator", default=None,)
	denominator: Optional[str] = Field(alias="denominator", default=None,)

