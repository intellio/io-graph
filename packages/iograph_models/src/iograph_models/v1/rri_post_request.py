from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RriPostRequest(BaseModel):
	nper: Optional[str] = Field(alias="nper", default=None,)
	pv: Optional[str] = Field(alias="pv", default=None,)
	fv: Optional[str] = Field(alias="fv", default=None,)

