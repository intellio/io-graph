from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConvertPostRequest(BaseModel):
	number: Optional[str] = Field(default=None,alias="number",)
	fromUnit: Optional[str] = Field(default=None,alias="fromUnit",)
	toUnit: Optional[str] = Field(default=None,alias="toUnit",)


