from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Odd_l_pricePostRequest(BaseModel):
	settlement: Optional[str] = Field(default=None,alias="settlement",)
	maturity: Optional[str] = Field(default=None,alias="maturity",)
	lastInterest: Optional[str] = Field(default=None,alias="lastInterest",)
	rate: Optional[str] = Field(default=None,alias="rate",)
	yld: Optional[str] = Field(default=None,alias="yld",)
	redemption: Optional[str] = Field(default=None,alias="redemption",)
	frequency: Optional[str] = Field(default=None,alias="frequency",)
	basis: Optional[str] = Field(default=None,alias="basis",)


