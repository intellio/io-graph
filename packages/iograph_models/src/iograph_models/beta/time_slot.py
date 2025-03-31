from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TimeSlot(BaseModel):
	end: Optional[DateTimeTimeZone] = Field(alias="end", default=None,)
	start: Optional[DateTimeTimeZone] = Field(alias="start", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .date_time_time_zone import DateTimeTimeZone
