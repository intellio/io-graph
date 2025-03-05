from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Yield_matPostRequest(BaseModel):
	settlement: Optional[str] = Field(default=None,alias="settlement",)
	maturity: Optional[str] = Field(default=None,alias="maturity",)
	issue: Optional[str] = Field(default=None,alias="issue",)
	rate: Optional[str] = Field(default=None,alias="rate",)
	pr: Optional[str] = Field(default=None,alias="pr",)
	basis: Optional[str] = Field(default=None,alias="basis",)


