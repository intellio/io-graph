from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Rank__eqPostRequest(BaseModel):
	number: Optional[str] = Field(alias="number", default=None,)
	ref: Optional[str] = Field(alias="ref", default=None,)
	order: Optional[str] = Field(alias="order", default=None,)

