from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TimeOffItem(BaseModel):
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	theme: Optional[ScheduleEntityTheme] = Field(default=None,alias="theme",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	timeOffReasonId: Optional[str] = Field(default=None,alias="timeOffReasonId",)

from .schedule_entity_theme import ScheduleEntityTheme

