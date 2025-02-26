from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Tbill_eqPostRequest(BaseModel):
	settlement: Optional[str] = Field(default=None,alias="settlement",)
	maturity: Optional[str] = Field(default=None,alias="maturity",)
	discount: Optional[str] = Field(default=None,alias="discount",)


