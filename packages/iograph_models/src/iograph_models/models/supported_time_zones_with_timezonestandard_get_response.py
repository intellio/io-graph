from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Supported_time_zones_with_timezonestandardGetResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[TimeZoneInformation]] = Field(default=None,alias="value",)

from .time_zone_information import TimeZoneInformation

