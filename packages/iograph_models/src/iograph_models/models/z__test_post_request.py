from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Z__testPostRequest(BaseModel):
	array: Optional[str] = Field(default=None,alias="array",)
	x: Optional[str] = Field(default=None,alias="x",)
	sigma: Optional[str] = Field(default=None,alias="sigma",)


