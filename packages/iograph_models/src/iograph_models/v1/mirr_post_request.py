from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MirrPostRequest(BaseModel):
	values: Optional[str] = Field(alias="values", default=None,)
	financeRate: Optional[str] = Field(alias="financeRate", default=None,)
	reinvestRate: Optional[str] = Field(alias="reinvestRate", default=None,)

