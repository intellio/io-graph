from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FixedPostRequest(BaseModel):
	number: Optional[str] = Field(default=None,alias="number",)
	decimals: Optional[str] = Field(default=None,alias="decimals",)
	noCommas: Optional[str] = Field(default=None,alias="noCommas",)


