from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_staff_availabilityPostRequest(BaseModel):
	staffIds: Optional[list[str]] = Field(alias="staffIds", default=None,)
	startDateTime: Optional[DateTimeTimeZone] = Field(alias="startDateTime", default=None,)
	endDateTime: Optional[DateTimeTimeZone] = Field(alias="endDateTime", default=None,)

from .date_time_time_zone import DateTimeTimeZone
