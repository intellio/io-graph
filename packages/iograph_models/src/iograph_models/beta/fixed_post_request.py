from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FixedPostRequest(BaseModel):
	number: Optional[str] = Field(alias="number", default=None,)
	decimals: Optional[str] = Field(alias="decimals", default=None,)
	noCommas: Optional[str] = Field(alias="noCommas", default=None,)

