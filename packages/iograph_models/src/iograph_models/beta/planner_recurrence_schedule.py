from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PlannerRecurrenceSchedule(BaseModel):
	nextOccurrenceDateTime: Optional[datetime] = Field(alias="nextOccurrenceDateTime", default=None,)
	pattern: Optional[RecurrencePattern] = Field(alias="pattern", default=None,)
	patternStartDateTime: Optional[datetime] = Field(alias="patternStartDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .recurrence_pattern import RecurrencePattern
