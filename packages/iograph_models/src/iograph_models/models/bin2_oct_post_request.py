from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Bin2_octPostRequest(BaseModel):
	number: Optional[str] = Field(default=None,alias="number",)
	places: Optional[str] = Field(default=None,alias="places",)


