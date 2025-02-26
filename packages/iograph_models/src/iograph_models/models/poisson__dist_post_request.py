from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Poisson__distPostRequest(BaseModel):
	x: Optional[str] = Field(default=None,alias="x",)
	mean: Optional[str] = Field(default=None,alias="mean",)
	cumulative: Optional[str] = Field(default=None,alias="cumulative",)


