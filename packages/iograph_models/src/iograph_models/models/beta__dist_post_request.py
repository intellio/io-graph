from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Beta__distPostRequest(BaseModel):
	x: Optional[str] = Field(default=None,alias="x",)
	alpha: Optional[str] = Field(default=None,alias="alpha",)
	beta: Optional[str] = Field(default=None,alias="beta",)
	cumulative: Optional[str] = Field(default=None,alias="cumulative",)
	A: Optional[str] = Field(default=None,alias="A",)
	B: Optional[str] = Field(default=None,alias="B",)


