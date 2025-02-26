from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Cum_i_pmtPostRequest(BaseModel):
	rate: Optional[str] = Field(default=None,alias="rate",)
	nper: Optional[str] = Field(default=None,alias="nper",)
	pv: Optional[str] = Field(default=None,alias="pv",)
	startPeriod: Optional[str] = Field(default=None,alias="startPeriod",)
	endPeriod: Optional[str] = Field(default=None,alias="endPeriod",)
	type: Optional[str] = Field(default=None,alias="type",)


