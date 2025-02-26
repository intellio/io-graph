from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TimeZoneInformation(BaseModel):
	alias: Optional[str] = Field(default=None,alias="alias",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


