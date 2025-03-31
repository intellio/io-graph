from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DurationPostRequest(BaseModel):
	settlement: Optional[str] = Field(alias="settlement", default=None,)
	maturity: Optional[str] = Field(alias="maturity", default=None,)
	coupon: Optional[str] = Field(alias="coupon", default=None,)
	yld: Optional[str] = Field(alias="yld", default=None,)
	frequency: Optional[str] = Field(alias="frequency", default=None,)
	basis: Optional[str] = Field(alias="basis", default=None,)

