from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DaylightTimeZoneOffset(BaseModel):
	dayOccurrence: Optional[int] = Field(alias="dayOccurrence",default=None,)
	dayOfWeek: Optional[str | DayOfWeek] = Field(alias="dayOfWeek",default=None,)
	month: Optional[int] = Field(alias="month",default=None,)
	time: Optional[str] = Field(alias="time",default=None,)
	year: Optional[int] = Field(alias="year",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	daylightBias: Optional[int] = Field(alias="daylightBias",default=None,)

from .day_of_week import DayOfWeek

