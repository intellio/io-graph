from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CustomTimeZone(BaseModel):
	name: Optional[str] = Field(default=None,alias="name",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	bias: Optional[int] = Field(default=None,alias="bias",)
	daylightOffset: Optional[DaylightTimeZoneOffset] = Field(default=None,alias="daylightOffset",)
	standardOffset: Optional[StandardTimeZoneOffset] = Field(default=None,alias="standardOffset",)

from .daylight_time_zone_offset import DaylightTimeZoneOffset
from .standard_time_zone_offset import StandardTimeZoneOffset

