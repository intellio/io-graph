from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Tbill_yieldPostRequest(BaseModel):
	settlement: Optional[str] = Field(alias="settlement", default=None,)
	maturity: Optional[str] = Field(alias="maturity", default=None,)
	pr: Optional[str] = Field(alias="pr", default=None,)

