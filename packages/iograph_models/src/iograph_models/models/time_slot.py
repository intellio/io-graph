from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TimeSlot(BaseModel):
	end: Optional[DateTimeTimeZone] = Field(default=None,alias="end",)
	start: Optional[DateTimeTimeZone] = Field(default=None,alias="start",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone

