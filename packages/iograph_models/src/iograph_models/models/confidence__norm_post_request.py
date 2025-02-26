from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Confidence__normPostRequest(BaseModel):
	alpha: Optional[str] = Field(default=None,alias="alpha",)
	standardDev: Optional[str] = Field(default=None,alias="standardDev",)
	size: Optional[str] = Field(default=None,alias="size",)


