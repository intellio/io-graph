from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Supported_time_zones_with_timezonestandardGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[TimeZoneInformation]] = Field(alias="value", default=None,)

from .time_zone_information import TimeZoneInformation
