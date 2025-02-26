from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Odd_f_yieldPostRequest(BaseModel):
	settlement: Optional[str] = Field(default=None,alias="settlement",)
	maturity: Optional[str] = Field(default=None,alias="maturity",)
	issue: Optional[str] = Field(default=None,alias="issue",)
	firstCoupon: Optional[str] = Field(default=None,alias="firstCoupon",)
	rate: Optional[str] = Field(default=None,alias="rate",)
	pr: Optional[str] = Field(default=None,alias="pr",)
	redemption: Optional[str] = Field(default=None,alias="redemption",)
	frequency: Optional[str] = Field(default=None,alias="frequency",)
	basis: Optional[str] = Field(default=None,alias="basis",)


