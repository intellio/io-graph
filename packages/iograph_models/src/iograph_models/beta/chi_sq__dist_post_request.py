from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Chi_sq__distPostRequest(BaseModel):
	x: Optional[str] = Field(alias="x", default=None,)
	degFreedom: Optional[str] = Field(alias="degFreedom", default=None,)
	cumulative: Optional[str] = Field(alias="cumulative", default=None,)

