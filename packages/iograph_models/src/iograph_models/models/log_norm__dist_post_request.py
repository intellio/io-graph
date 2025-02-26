from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Log_norm__distPostRequest(BaseModel):
	x: Optional[str] = Field(default=None,alias="x",)
	mean: Optional[str] = Field(default=None,alias="mean",)
	standardDev: Optional[str] = Field(default=None,alias="standardDev",)
	cumulative: Optional[str] = Field(default=None,alias="cumulative",)


