from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DiscPostRequest(BaseModel):
	settlement: Optional[str] = Field(alias="settlement", default=None,)
	maturity: Optional[str] = Field(alias="maturity", default=None,)
	pr: Optional[str] = Field(alias="pr", default=None,)
	redemption: Optional[str] = Field(alias="redemption", default=None,)
	basis: Optional[str] = Field(alias="basis", default=None,)

