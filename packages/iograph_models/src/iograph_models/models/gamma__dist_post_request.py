from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Gamma__distPostRequest(BaseModel):
	x: Optional[str] = Field(default=None,alias="x",)
	alpha: Optional[str] = Field(default=None,alias="alpha",)
	beta: Optional[str] = Field(default=None,alias="beta",)
	cumulative: Optional[str] = Field(default=None,alias="cumulative",)


