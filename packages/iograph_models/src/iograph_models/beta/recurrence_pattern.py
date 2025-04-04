from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RecurrencePattern(BaseModel):
	dayOfMonth: Optional[int] = Field(alias="dayOfMonth", default=None,)
	daysOfWeek: Optional[list[DayOfWeek | str]] = Field(alias="daysOfWeek", default=None,)
	firstDayOfWeek: Optional[DayOfWeek | str] = Field(alias="firstDayOfWeek", default=None,)
	index: Optional[WeekIndex | str] = Field(alias="index", default=None,)
	interval: Optional[int] = Field(alias="interval", default=None,)
	month: Optional[int] = Field(alias="month", default=None,)
	type: Optional[RecurrencePatternType | str] = Field(alias="type", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .day_of_week import DayOfWeek
from .week_index import WeekIndex
from .recurrence_pattern_type import RecurrencePatternType
