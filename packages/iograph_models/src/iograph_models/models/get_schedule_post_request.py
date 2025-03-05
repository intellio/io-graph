from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_schedulePostRequest(BaseModel):
	Schedules: Optional[list[str]] = Field(alias="Schedules",default=None,)
	EndTime: Optional[DateTimeTimeZone] = Field(alias="EndTime",default=None,)
	StartTime: Optional[DateTimeTimeZone] = Field(alias="StartTime",default=None,)
	AvailabilityViewInterval: Optional[int] = Field(alias="AvailabilityViewInterval",default=None,)

from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone

