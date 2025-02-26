from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Floor__precisePostRequest(BaseModel):
	number: Optional[str] = Field(default=None,alias="number",)
	significance: Optional[str] = Field(default=None,alias="significance",)


