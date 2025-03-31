from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class WorkingHours(BaseModel):
	daysOfWeek: Optional[list[DayOfWeek | str]] = Field(alias="daysOfWeek", default=None,)
	endTime: Optional[str] = Field(alias="endTime", default=None,)
	startTime: Optional[str] = Field(alias="startTime", default=None,)
	timeZone: Optional[Union[CustomTimeZone]] = Field(alias="timeZone", default=None,discriminator="odata_type", )
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .day_of_week import DayOfWeek
from .custom_time_zone import CustomTimeZone
