from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ScheduleItem(BaseModel):
	end: Optional[DateTimeTimeZone] = Field(default=None,alias="end",)
	isPrivate: Optional[bool] = Field(default=None,alias="isPrivate",)
	location: Optional[str] = Field(default=None,alias="location",)
	start: Optional[DateTimeTimeZone] = Field(default=None,alias="start",)
	status: Optional[FreeBusyStatus] = Field(default=None,alias="status",)
	subject: Optional[str] = Field(default=None,alias="subject",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone
from .free_busy_status import FreeBusyStatus

