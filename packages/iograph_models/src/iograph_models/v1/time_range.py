from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TimeRange(BaseModel):
	endTime: Optional[str] = Field(alias="endTime", default=None,)
	startTime: Optional[str] = Field(alias="startTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

