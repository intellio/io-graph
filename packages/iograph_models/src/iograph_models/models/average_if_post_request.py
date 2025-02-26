from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Average_ifPostRequest(BaseModel):
	range: Optional[str] = Field(default=None,alias="range",)
	criteria: Optional[str] = Field(default=None,alias="criteria",)
	averageRange: Optional[str] = Field(default=None,alias="averageRange",)


