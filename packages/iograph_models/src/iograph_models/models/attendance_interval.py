from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AttendanceInterval(BaseModel):
	durationInSeconds: Optional[int] = Field(default=None,alias="durationInSeconds",)
	joinDateTime: Optional[datetime] = Field(default=None,alias="joinDateTime",)
	leaveDateTime: Optional[datetime] = Field(default=None,alias="leaveDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


