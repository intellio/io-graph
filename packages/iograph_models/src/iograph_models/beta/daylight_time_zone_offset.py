from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DaylightTimeZoneOffset(BaseModel):
	dayOccurrence: Optional[int] = Field(alias="dayOccurrence", default=None,)
	dayOfWeek: Optional[DayOfWeek | str] = Field(alias="dayOfWeek", default=None,)
	month: Optional[int] = Field(alias="month", default=None,)
	time: Optional[str] = Field(alias="time", default=None,)
	year: Optional[int] = Field(alias="year", default=None,)
	odata_type: Literal["#microsoft.graph.daylightTimeZoneOffset"] = Field(alias="@odata.type", default="#microsoft.graph.daylightTimeZoneOffset")
	daylightBias: Optional[int] = Field(alias="daylightBias", default=None,)

from .day_of_week import DayOfWeek

