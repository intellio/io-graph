from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ShiftAvailability(BaseModel):
	recurrence: Optional[PatternedRecurrence] = Field(alias="recurrence", default=None,)
	timeSlots: Optional[list[TimeRange]] = Field(alias="timeSlots", default=None,)
	timeZone: Optional[str] = Field(alias="timeZone", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .patterned_recurrence import PatternedRecurrence
from .time_range import TimeRange

