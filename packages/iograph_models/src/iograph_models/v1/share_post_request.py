from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SharePostRequest(BaseModel):
	notifyTeam: Optional[bool] = Field(alias="notifyTeam", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)

