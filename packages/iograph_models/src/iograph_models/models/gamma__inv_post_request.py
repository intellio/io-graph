from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Gamma__invPostRequest(BaseModel):
	probability: Optional[str] = Field(default=None,alias="probability",)
	alpha: Optional[str] = Field(default=None,alias="alpha",)
	beta: Optional[str] = Field(default=None,alias="beta",)


