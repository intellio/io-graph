from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SharePostRequest(BaseModel):
	notifyTeam: Optional[bool] = Field(default=None,alias="notifyTeam",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)


