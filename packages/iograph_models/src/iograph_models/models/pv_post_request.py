from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PvPostRequest(BaseModel):
	rate: Optional[str] = Field(default=None,alias="rate",)
	nper: Optional[str] = Field(default=None,alias="nper",)
	pmt: Optional[str] = Field(default=None,alias="pmt",)
	fv: Optional[str] = Field(default=None,alias="fv",)
	type: Optional[str] = Field(default=None,alias="type",)


