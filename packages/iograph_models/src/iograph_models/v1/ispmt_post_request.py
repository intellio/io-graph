from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IspmtPostRequest(BaseModel):
	rate: Optional[str] = Field(alias="rate", default=None,)
	per: Optional[str] = Field(alias="per", default=None,)
	nper: Optional[str] = Field(alias="nper", default=None,)
	pv: Optional[str] = Field(alias="pv", default=None,)


