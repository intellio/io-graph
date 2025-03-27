from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PmtPostRequest(BaseModel):
	rate: Optional[str] = Field(alias="rate", default=None,)
	nper: Optional[str] = Field(alias="nper", default=None,)
	pv: Optional[str] = Field(alias="pv", default=None,)
	fv: Optional[str] = Field(alias="fv", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)


