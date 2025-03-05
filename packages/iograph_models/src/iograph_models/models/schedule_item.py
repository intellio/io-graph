from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ScheduleItem(BaseModel):
	end: Optional[DateTimeTimeZone] = Field(alias="end",default=None,)
	isPrivate: Optional[bool] = Field(alias="isPrivate",default=None,)
	location: Optional[str] = Field(alias="location",default=None,)
	start: Optional[DateTimeTimeZone] = Field(alias="start",default=None,)
	status: Optional[str | FreeBusyStatus] = Field(alias="status",default=None,)
	subject: Optional[str] = Field(alias="subject",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone
from .free_busy_status import FreeBusyStatus

