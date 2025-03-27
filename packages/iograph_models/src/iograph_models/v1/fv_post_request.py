from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FvPostRequest(BaseModel):
	rate: Optional[str] = Field(alias="rate", default=None,)
	nper: Optional[str] = Field(alias="nper", default=None,)
	pmt: Optional[str] = Field(alias="pmt", default=None,)
	pv: Optional[str] = Field(alias="pv", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)


