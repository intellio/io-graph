from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Beta__invPostRequest(BaseModel):
	probability: Optional[str] = Field(default=None,alias="probability",)
	alpha: Optional[str] = Field(default=None,alias="alpha",)
	beta: Optional[str] = Field(default=None,alias="beta",)
	A: Optional[str] = Field(default=None,alias="A",)
	B: Optional[str] = Field(default=None,alias="B",)


