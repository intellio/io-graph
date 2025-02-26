from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BitrshiftPostRequest(BaseModel):
	number: Optional[str] = Field(default=None,alias="number",)
	shiftAmount: Optional[str] = Field(default=None,alias="shiftAmount",)


