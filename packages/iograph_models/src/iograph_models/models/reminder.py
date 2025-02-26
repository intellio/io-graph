from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Reminder(BaseModel):
	changeKey: Optional[str] = Field(default=None,alias="changeKey",)
	eventEndTime: Optional[DateTimeTimeZone] = Field(default=None,alias="eventEndTime",)
	eventId: Optional[str] = Field(default=None,alias="eventId",)
	eventLocation: Optional[Location] = Field(default=None,alias="eventLocation",)
	eventStartTime: Optional[DateTimeTimeZone] = Field(default=None,alias="eventStartTime",)
	eventSubject: Optional[str] = Field(default=None,alias="eventSubject",)
	eventWebLink: Optional[str] = Field(default=None,alias="eventWebLink",)
	reminderFireTime: Optional[DateTimeTimeZone] = Field(default=None,alias="reminderFireTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .date_time_time_zone import DateTimeTimeZone
from .location import Location
from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone

