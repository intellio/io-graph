from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DaylightTimeZoneOffset(BaseModel):
	dayOccurrence: Optional[int] = Field(default=None,alias="dayOccurrence",)
	dayOfWeek: Optional[DayOfWeek] = Field(default=None,alias="dayOfWeek",)
	month: Optional[int] = Field(default=None,alias="month",)
	time: Optional[str] = Field(default=None,alias="time",)
	year: Optional[int] = Field(default=None,alias="year",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	daylightBias: Optional[int] = Field(default=None,alias="daylightBias",)

from .day_of_week import DayOfWeek

