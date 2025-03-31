from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BitrshiftPostRequest(BaseModel):
	number: Optional[str] = Field(alias="number", default=None,)
	shiftAmount: Optional[str] = Field(alias="shiftAmount", default=None,)

