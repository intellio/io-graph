from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RatePostRequest(BaseModel):
	nper: Optional[str] = Field(default=None,alias="nper",)
	pmt: Optional[str] = Field(default=None,alias="pmt",)
	pv: Optional[str] = Field(default=None,alias="pv",)
	fv: Optional[str] = Field(default=None,alias="fv",)
	type: Optional[str] = Field(default=None,alias="type",)
	guess: Optional[str] = Field(default=None,alias="guess",)


