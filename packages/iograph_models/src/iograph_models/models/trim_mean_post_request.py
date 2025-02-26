from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Trim_meanPostRequest(BaseModel):
	array: Optional[str] = Field(default=None,alias="array",)
	percent: Optional[str] = Field(default=None,alias="percent",)


