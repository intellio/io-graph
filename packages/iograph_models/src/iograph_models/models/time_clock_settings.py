from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TimeClockSettings(BaseModel):
	approvedLocation: Optional[GeoCoordinates] = Field(default=None,alias="approvedLocation",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .geo_coordinates import GeoCoordinates

