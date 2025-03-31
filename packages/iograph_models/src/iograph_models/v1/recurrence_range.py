from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RecurrenceRange(BaseModel):
	endDate: Optional[str] = Field(alias="endDate", default=None,)
	numberOfOccurrences: Optional[int] = Field(alias="numberOfOccurrences", default=None,)
	recurrenceTimeZone: Optional[str] = Field(alias="recurrenceTimeZone", default=None,)
	startDate: Optional[str] = Field(alias="startDate", default=None,)
	type: Optional[RecurrenceRangeType | str] = Field(alias="type", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .recurrence_range_type import RecurrenceRangeType
