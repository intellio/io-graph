from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PvPostRequest(BaseModel):
	rate: Optional[str] = Field(alias="rate",default=None,)
	nper: Optional[str] = Field(alias="nper",default=None,)
	pmt: Optional[str] = Field(alias="pmt",default=None,)
	fv: Optional[str] = Field(alias="fv",default=None,)
	type: Optional[str] = Field(alias="type",default=None,)


