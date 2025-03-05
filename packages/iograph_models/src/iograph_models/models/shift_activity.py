from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ShiftActivity(BaseModel):
	code: Optional[str] = Field(alias="code",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime",default=None,)
	isPaid: Optional[bool] = Field(alias="isPaid",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	theme: Optional[str | ScheduleEntityTheme] = Field(alias="theme",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .schedule_entity_theme import ScheduleEntityTheme

