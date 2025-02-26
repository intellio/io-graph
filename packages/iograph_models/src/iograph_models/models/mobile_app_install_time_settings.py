from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MobileAppInstallTimeSettings(BaseModel):
	deadlineDateTime: Optional[datetime] = Field(default=None,alias="deadlineDateTime",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	useLocalTime: Optional[bool] = Field(default=None,alias="useLocalTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


