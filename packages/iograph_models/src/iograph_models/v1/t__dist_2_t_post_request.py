from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class T__dist_2_tPostRequest(BaseModel):
	x: Optional[str] = Field(alias="x", default=None,)
	degFreedom: Optional[str] = Field(alias="degFreedom", default=None,)

