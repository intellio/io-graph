from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Erf_cPostRequest(BaseModel):
	x: Optional[str] = Field(default=None,alias="x",)


