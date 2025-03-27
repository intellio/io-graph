from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrinterLocation(BaseModel):
	altitudeInMeters: Optional[int] = Field(alias="altitudeInMeters", default=None,)
	building: Optional[str] = Field(alias="building", default=None,)
	city: Optional[str] = Field(alias="city", default=None,)
	countryOrRegion: Optional[str] = Field(alias="countryOrRegion", default=None,)
	floor: Optional[str] = Field(alias="floor", default=None,)
	floorDescription: Optional[str] = Field(alias="floorDescription", default=None,)
	floorNumber: Optional[int] = Field(alias="floorNumber", default=None,)
	latitude: float | str | ReferenceNumeric
	longitude: float | str | ReferenceNumeric
	organization: Optional[list[str]] = Field(alias="organization", default=None,)
	postalCode: Optional[str] = Field(alias="postalCode", default=None,)
	roomDescription: Optional[str] = Field(alias="roomDescription", default=None,)
	roomName: Optional[str] = Field(alias="roomName", default=None,)
	roomNumber: Optional[int] = Field(alias="roomNumber", default=None,)
	site: Optional[str] = Field(alias="site", default=None,)
	stateOrProvince: Optional[str] = Field(alias="stateOrProvince", default=None,)
	streetAddress: Optional[str] = Field(alias="streetAddress", default=None,)
	subdivision: Optional[list[str]] = Field(alias="subdivision", default=None,)
	subunit: Optional[list[str]] = Field(alias="subunit", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

