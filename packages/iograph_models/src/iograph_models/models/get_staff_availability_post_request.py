from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_staff_availabilityPostRequest(BaseModel):
	staffIds: list[str] = Field(alias="staffIds",)
	startDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="startDateTime",)
	endDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="endDateTime",)

from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone

