from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FvPostRequest(BaseModel):
	rate: Optional[str] = Field(default=None,alias="rate",)
	nper: Optional[str] = Field(default=None,alias="nper",)
	pmt: Optional[str] = Field(default=None,alias="pmt",)
	pv: Optional[str] = Field(default=None,alias="pv",)
	type: Optional[str] = Field(default=None,alias="type",)


