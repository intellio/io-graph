from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DurationPostRequest(BaseModel):
	settlement: Optional[str] = Field(default=None,alias="settlement",)
	maturity: Optional[str] = Field(default=None,alias="maturity",)
	coupon: Optional[str] = Field(default=None,alias="coupon",)
	yld: Optional[str] = Field(default=None,alias="yld",)
	frequency: Optional[str] = Field(default=None,alias="frequency",)
	basis: Optional[str] = Field(default=None,alias="basis",)


