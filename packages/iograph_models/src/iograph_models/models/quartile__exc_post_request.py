from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Quartile__excPostRequest(BaseModel):
	array: Optional[str] = Field(default=None,alias="array",)
	quart: Optional[str] = Field(default=None,alias="quart",)


