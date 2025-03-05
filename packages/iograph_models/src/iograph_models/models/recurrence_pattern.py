from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RecurrencePattern(BaseModel):
	dayOfMonth: Optional[int] = Field(default=None,alias="dayOfMonth",)
	daysOfWeek: Optional[DayOfWeek] = Field(default=None,alias="daysOfWeek",)
	firstDayOfWeek: Optional[DayOfWeek] = Field(default=None,alias="firstDayOfWeek",)
	index: Optional[WeekIndex] = Field(default=None,alias="index",)
	interval: Optional[int] = Field(default=None,alias="interval",)
	month: Optional[int] = Field(default=None,alias="month",)
	type: Optional[RecurrencePatternType] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .day_of_week import DayOfWeek
from .day_of_week import DayOfWeek
from .week_index import WeekIndex
from .recurrence_pattern_type import RecurrencePatternType

