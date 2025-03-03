from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Rank__eqPostRequest(BaseModel):
	number: Optional[str] = Field(default=None,alias="number",)
	ref: Optional[str] = Field(default=None,alias="ref",)
	order: Optional[str] = Field(default=None,alias="order",)


