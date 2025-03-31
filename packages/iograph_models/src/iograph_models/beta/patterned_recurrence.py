from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PatternedRecurrence(BaseModel):
	pattern: Optional[RecurrencePattern] = Field(alias="pattern", default=None,)
	range: Optional[RecurrenceRange] = Field(alias="range", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .recurrence_pattern import RecurrencePattern
from .recurrence_range import RecurrenceRange
