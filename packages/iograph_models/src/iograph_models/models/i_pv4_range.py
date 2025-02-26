from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IPv4Range(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	lowerAddress: Optional[str] = Field(default=None,alias="lowerAddress",)
	upperAddress: Optional[str] = Field(default=None,alias="upperAddress",)


