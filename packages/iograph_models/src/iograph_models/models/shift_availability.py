from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ShiftAvailability(BaseModel):
	recurrence: Optional[PatternedRecurrence] = Field(default=None,alias="recurrence",)
	timeSlots: Optional[list[TimeRange]] = Field(default=None,alias="timeSlots",)
	timeZone: Optional[str] = Field(default=None,alias="timeZone",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .patterned_recurrence import PatternedRecurrence
from .time_range import TimeRange

