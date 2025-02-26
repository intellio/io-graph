from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Percent_rank__incPostRequest(BaseModel):
	array: Optional[str] = Field(default=None,alias="array",)
	x: Optional[str] = Field(default=None,alias="x",)
	significance: Optional[str] = Field(default=None,alias="significance",)


