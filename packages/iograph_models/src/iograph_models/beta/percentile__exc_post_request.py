from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Percentile__excPostRequest(BaseModel):
	array: Optional[str] = Field(alias="array", default=None,)
	k: Optional[str] = Field(alias="k", default=None,)

