from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SignInLocation(BaseModel):
	city: Optional[str] = Field(alias="city", default=None,)
	countryOrRegion: Optional[str] = Field(alias="countryOrRegion", default=None,)
	geoCoordinates: Optional[GeoCoordinates] = Field(alias="geoCoordinates", default=None,)
	state: Optional[str] = Field(alias="state", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .geo_coordinates import GeoCoordinates
