from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RecurrenceRange(BaseModel):
	endDate: Optional[str] = Field(default=None,alias="endDate",)
	numberOfOccurrences: Optional[int] = Field(default=None,alias="numberOfOccurrences",)
	recurrenceTimeZone: Optional[str] = Field(default=None,alias="recurrenceTimeZone",)
	startDate: Optional[str] = Field(default=None,alias="startDate",)
	type: Optional[RecurrenceRangeType] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .recurrence_range_type import RecurrenceRangeType

