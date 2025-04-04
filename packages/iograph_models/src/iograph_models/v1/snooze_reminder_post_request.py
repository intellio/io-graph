from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Snooze_reminderPostRequest(BaseModel):
	NewReminderTime: Optional[DateTimeTimeZone] = Field(alias="NewReminderTime", default=None,)

from .date_time_time_zone import DateTimeTimeZone
