from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Rand_betweenPostRequest(BaseModel):
	bottom: Optional[str] = Field(alias="bottom", default=None,)
	top: Optional[str] = Field(alias="top", default=None,)

