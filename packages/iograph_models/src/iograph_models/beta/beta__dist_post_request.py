from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Beta__distPostRequest(BaseModel):
	x: Optional[str] = Field(alias="x", default=None,)
	alpha: Optional[str] = Field(alias="alpha", default=None,)
	beta: Optional[str] = Field(alias="beta", default=None,)
	cumulative: Optional[str] = Field(alias="cumulative", default=None,)
	A: Optional[str] = Field(alias="A", default=None,)
	B: Optional[str] = Field(alias="B", default=None,)

