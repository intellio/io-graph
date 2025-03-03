from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_schedulePostRequest(BaseModel):
	Schedules: Optional[list[str]] = Field(default=None,alias="Schedules",)
	EndTime: Optional[DateTimeTimeZone] = Field(default=None,alias="EndTime",)
	StartTime: Optional[DateTimeTimeZone] = Field(default=None,alias="StartTime",)
	AvailabilityViewInterval: Optional[int] = Field(default=None,alias="AvailabilityViewInterval",)

from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone

