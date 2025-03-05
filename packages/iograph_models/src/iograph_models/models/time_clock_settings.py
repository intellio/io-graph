from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TimeClockSettings(BaseModel):
	approvedLocation: Optional[GeoCoordinates] = Field(alias="approvedLocation",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .geo_coordinates import GeoCoordinates

