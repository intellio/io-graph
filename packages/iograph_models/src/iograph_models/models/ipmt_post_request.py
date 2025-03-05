from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IpmtPostRequest(BaseModel):
	rate: Optional[str] = Field(default=None,alias="rate",)
	per: Optional[str] = Field(default=None,alias="per",)
	nper: Optional[str] = Field(default=None,alias="nper",)
	pv: Optional[str] = Field(default=None,alias="pv",)
	fv: Optional[str] = Field(default=None,alias="fv",)
	type: Optional[str] = Field(default=None,alias="type",)


