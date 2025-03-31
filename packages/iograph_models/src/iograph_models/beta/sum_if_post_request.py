from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Sum_ifPostRequest(BaseModel):
	range: Optional[str] = Field(alias="range", default=None,)
	criteria: Optional[str] = Field(alias="criteria", default=None,)
	sumRange: Optional[str] = Field(alias="sumRange", default=None,)

