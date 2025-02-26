from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Yield_discPostRequest(BaseModel):
	settlement: Optional[str] = Field(default=None,alias="settlement",)
	maturity: Optional[str] = Field(default=None,alias="maturity",)
	pr: Optional[str] = Field(default=None,alias="pr",)
	redemption: Optional[str] = Field(default=None,alias="redemption",)
	basis: Optional[str] = Field(default=None,alias="basis",)


