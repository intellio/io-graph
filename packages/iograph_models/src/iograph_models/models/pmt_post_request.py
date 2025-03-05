from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PmtPostRequest(BaseModel):
	rate: Optional[str] = Field(default=None,alias="rate",)
	nper: Optional[str] = Field(default=None,alias="nper",)
	pv: Optional[str] = Field(default=None,alias="pv",)
	fv: Optional[str] = Field(default=None,alias="fv",)
	type: Optional[str] = Field(default=None,alias="type",)


