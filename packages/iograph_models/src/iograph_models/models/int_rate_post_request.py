from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Int_ratePostRequest(BaseModel):
	settlement: Optional[str] = Field(default=None,alias="settlement",)
	maturity: Optional[str] = Field(default=None,alias="maturity",)
	investment: Optional[str] = Field(default=None,alias="investment",)
	redemption: Optional[str] = Field(default=None,alias="redemption",)
	basis: Optional[str] = Field(default=None,alias="basis",)


