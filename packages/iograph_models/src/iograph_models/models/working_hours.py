from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkingHours(BaseModel):
	daysOfWeek: Optional[str | DayOfWeek] = Field(alias="daysOfWeek",default=None,)
	endTime: Optional[str] = Field(alias="endTime",default=None,)
	startTime: Optional[str] = Field(alias="startTime",default=None,)
	timeZone: SerializeAsAny[Optional[TimeZoneBase]] = Field(alias="timeZone",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .day_of_week import DayOfWeek
from .time_zone_base import TimeZoneBase

