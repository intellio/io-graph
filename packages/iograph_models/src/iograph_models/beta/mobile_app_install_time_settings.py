from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MobileAppInstallTimeSettings(BaseModel):
	deadlineDateTime: Optional[datetime] = Field(alias="deadlineDateTime", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	useLocalTime: Optional[bool] = Field(alias="useLocalTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

