from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RatePostRequest(BaseModel):
	nper: Optional[str] = Field(alias="nper", default=None,)
	pmt: Optional[str] = Field(alias="pmt", default=None,)
	pv: Optional[str] = Field(alias="pv", default=None,)
	fv: Optional[str] = Field(alias="fv", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	guess: Optional[str] = Field(alias="guess", default=None,)


