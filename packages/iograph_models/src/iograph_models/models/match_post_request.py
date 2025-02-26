from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MatchPostRequest(BaseModel):
	lookupValue: Optional[str] = Field(default=None,alias="lookupValue",)
	lookupArray: Optional[str] = Field(default=None,alias="lookupArray",)
	matchType: Optional[str] = Field(default=None,alias="matchType",)


