from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class CustomTimeZone(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	odata_type: Literal["#microsoft.graph.customTimeZone"] = Field(alias="@odata.type", default="#microsoft.graph.customTimeZone")
	bias: Optional[int] = Field(alias="bias", default=None,)
	daylightOffset: Optional[DaylightTimeZoneOffset] = Field(alias="daylightOffset", default=None,)
	standardOffset: Optional[Union[DaylightTimeZoneOffset]] = Field(alias="standardOffset", default=None,discriminator="odata_type", )

from .daylight_time_zone_offset import DaylightTimeZoneOffset
from .daylight_time_zone_offset import DaylightTimeZoneOffset

