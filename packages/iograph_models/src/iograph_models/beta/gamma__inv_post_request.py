from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Gamma__invPostRequest(BaseModel):
	probability: Optional[str] = Field(alias="probability", default=None,)
	alpha: Optional[str] = Field(alias="alpha", default=None,)
	beta: Optional[str] = Field(alias="beta", default=None,)

