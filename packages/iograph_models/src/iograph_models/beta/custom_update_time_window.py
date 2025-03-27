from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomUpdateTimeWindow(BaseModel):
	endDay: Optional[DayOfWeek | str] = Field(alias="endDay", default=None,)
	endTime: Optional[str] = Field(alias="endTime", default=None,)
	startDay: Optional[DayOfWeek | str] = Field(alias="startDay", default=None,)
	startTime: Optional[str] = Field(alias="startTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .day_of_week import DayOfWeek
from .day_of_week import DayOfWeek

