from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TimePeriod(BaseModel):
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


