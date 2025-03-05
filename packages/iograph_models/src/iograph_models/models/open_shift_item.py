from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OpenShiftItem(BaseModel):
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	theme: Optional[ScheduleEntityTheme] = Field(default=None,alias="theme",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activities: Optional[list[ShiftActivity]] = Field(default=None,alias="activities",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	notes: Optional[str] = Field(default=None,alias="notes",)
	openSlotCount: Optional[int] = Field(default=None,alias="openSlotCount",)

from .schedule_entity_theme import ScheduleEntityTheme
from .shift_activity import ShiftActivity

