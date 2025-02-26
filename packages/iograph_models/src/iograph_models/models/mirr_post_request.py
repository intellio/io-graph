from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MirrPostRequest(BaseModel):
	values: Optional[str] = Field(default=None,alias="values",)
	financeRate: Optional[str] = Field(default=None,alias="financeRate",)
	reinvestRate: Optional[str] = Field(default=None,alias="reinvestRate",)


