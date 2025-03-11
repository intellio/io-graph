from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomTimeZone(BaseModel):
	name: Optional[str] = Field(alias="name",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	bias: Optional[int] = Field(alias="bias",default=None,)
	daylightOffset: Optional[DaylightTimeZoneOffset] = Field(alias="daylightOffset",default=None,)
	standardOffset: SerializeAsAny[Optional[StandardTimeZoneOffset]] = Field(alias="standardOffset",default=None,)

from .daylight_time_zone_offset import DaylightTimeZoneOffset
from .standard_time_zone_offset import StandardTimeZoneOffset

