from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SignInLocation(BaseModel):
	city: Optional[str] = Field(default=None,alias="city",)
	countryOrRegion: Optional[str] = Field(default=None,alias="countryOrRegion",)
	geoCoordinates: Optional[GeoCoordinates] = Field(default=None,alias="geoCoordinates",)
	state: Optional[str] = Field(default=None,alias="state",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .geo_coordinates import GeoCoordinates

