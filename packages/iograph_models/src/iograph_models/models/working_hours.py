from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkingHours(BaseModel):
	daysOfWeek: Optional[DayOfWeek] = Field(default=None,alias="daysOfWeek",)
	endTime: Optional[str] = Field(default=None,alias="endTime",)
	startTime: Optional[str] = Field(default=None,alias="startTime",)
	timeZone: SerializeAsAny[Optional[TimeZoneBase]] = Field(default=None,alias="timeZone",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .day_of_week import DayOfWeek
from .time_zone_base import TimeZoneBase

