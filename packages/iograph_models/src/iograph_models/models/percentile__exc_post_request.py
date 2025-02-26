from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Percentile__excPostRequest(BaseModel):
	array: Optional[str] = Field(default=None,alias="array",)
	k: Optional[str] = Field(default=None,alias="k",)


