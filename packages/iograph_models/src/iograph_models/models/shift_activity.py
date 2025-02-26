from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ShiftActivity(BaseModel):
	code: Optional[str] = Field(default=None,alias="code",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	isPaid: Optional[bool] = Field(default=None,alias="isPaid",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	theme: Optional[ScheduleEntityTheme] = Field(default=None,alias="theme",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .schedule_entity_theme import ScheduleEntityTheme

