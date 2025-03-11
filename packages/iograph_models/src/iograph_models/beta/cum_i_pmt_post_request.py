from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Cum_i_pmtPostRequest(BaseModel):
	rate: Optional[str] = Field(alias="rate",default=None,)
	nper: Optional[str] = Field(alias="nper",default=None,)
	pv: Optional[str] = Field(alias="pv",default=None,)
	startPeriod: Optional[str] = Field(alias="startPeriod",default=None,)
	endPeriod: Optional[str] = Field(alias="endPeriod",default=None,)
	type: Optional[str] = Field(alias="type",default=None,)


