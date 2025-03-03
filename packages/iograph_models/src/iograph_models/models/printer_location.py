from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrinterLocation(BaseModel):
	altitudeInMeters: Optional[int] = Field(default=None,alias="altitudeInMeters",)
	building: Optional[str] = Field(default=None,alias="building",)
	city: Optional[str] = Field(default=None,alias="city",)
	countryOrRegion: Optional[str] = Field(default=None,alias="countryOrRegion",)
	floor: Optional[str] = Field(default=None,alias="floor",)
	floorDescription: Optional[str] = Field(default=None,alias="floorDescription",)
	latitude: float | str | ReferenceNumeric
	longitude: float | str | ReferenceNumeric
	organization: Optional[list[str]] = Field(default=None,alias="organization",)
	postalCode: Optional[str] = Field(default=None,alias="postalCode",)
	roomDescription: Optional[str] = Field(default=None,alias="roomDescription",)
	roomName: Optional[str] = Field(default=None,alias="roomName",)
	site: Optional[str] = Field(default=None,alias="site",)
	stateOrProvince: Optional[str] = Field(default=None,alias="stateOrProvince",)
	streetAddress: Optional[str] = Field(default=None,alias="streetAddress",)
	subdivision: Optional[list[str]] = Field(default=None,alias="subdivision",)
	subunit: Optional[list[str]] = Field(default=None,alias="subunit",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

