from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PatternedRecurrence(BaseModel):
	pattern: Optional[RecurrencePattern] = Field(default=None,alias="pattern",)
	range: Optional[RecurrenceRange] = Field(default=None,alias="range",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .recurrence_pattern import RecurrencePattern
from .recurrence_range import RecurrenceRange

