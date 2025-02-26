from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ReceivedPostRequest(BaseModel):
	settlement: Optional[str] = Field(default=None,alias="settlement",)
	maturity: Optional[str] = Field(default=None,alias="maturity",)
	investment: Optional[str] = Field(default=None,alias="investment",)
	discount: Optional[str] = Field(default=None,alias="discount",)
	basis: Optional[str] = Field(default=None,alias="basis",)


