from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Price_matPostRequest(BaseModel):
	settlement: Optional[str] = Field(default=None,alias="settlement",)
	maturity: Optional[str] = Field(default=None,alias="maturity",)
	issue: Optional[str] = Field(default=None,alias="issue",)
	rate: Optional[str] = Field(default=None,alias="rate",)
	yld: Optional[str] = Field(default=None,alias="yld",)
	basis: Optional[str] = Field(default=None,alias="basis",)


