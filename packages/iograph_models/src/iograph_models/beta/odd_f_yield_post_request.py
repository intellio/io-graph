from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Odd_f_yieldPostRequest(BaseModel):
	settlement: Optional[str] = Field(alias="settlement", default=None,)
	maturity: Optional[str] = Field(alias="maturity", default=None,)
	issue: Optional[str] = Field(alias="issue", default=None,)
	firstCoupon: Optional[str] = Field(alias="firstCoupon", default=None,)
	rate: Optional[str] = Field(alias="rate", default=None,)
	pr: Optional[str] = Field(alias="pr", default=None,)
	redemption: Optional[str] = Field(alias="redemption", default=None,)
	frequency: Optional[str] = Field(alias="frequency", default=None,)
	basis: Optional[str] = Field(alias="basis", default=None,)


