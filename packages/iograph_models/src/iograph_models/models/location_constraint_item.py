from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LocationConstraintItem(BaseModel):
	address: Optional[PhysicalAddress] = Field(alias="address",default=None,)
	coordinates: Optional[OutlookGeoCoordinates] = Field(alias="coordinates",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	locationEmailAddress: Optional[str] = Field(alias="locationEmailAddress",default=None,)
	locationType: Optional[str | LocationType] = Field(alias="locationType",default=None,)
	locationUri: Optional[str] = Field(alias="locationUri",default=None,)
	uniqueId: Optional[str] = Field(alias="uniqueId",default=None,)
	uniqueIdType: Optional[str | LocationUniqueIdType] = Field(alias="uniqueIdType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	resolveAvailability: Optional[bool] = Field(alias="resolveAvailability",default=None,)

from .physical_address import PhysicalAddress
from .outlook_geo_coordinates import OutlookGeoCoordinates
from .location_type import LocationType
from .location_unique_id_type import LocationUniqueIdType

