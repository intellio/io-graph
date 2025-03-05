from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LocationConstraintItem(BaseModel):
	address: Optional[PhysicalAddress] = Field(default=None,alias="address",)
	coordinates: Optional[OutlookGeoCoordinates] = Field(default=None,alias="coordinates",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	locationEmailAddress: Optional[str] = Field(default=None,alias="locationEmailAddress",)
	locationType: Optional[LocationType] = Field(default=None,alias="locationType",)
	locationUri: Optional[str] = Field(default=None,alias="locationUri",)
	uniqueId: Optional[str] = Field(default=None,alias="uniqueId",)
	uniqueIdType: Optional[LocationUniqueIdType] = Field(default=None,alias="uniqueIdType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	resolveAvailability: Optional[bool] = Field(default=None,alias="resolveAvailability",)

from .physical_address import PhysicalAddress
from .outlook_geo_coordinates import OutlookGeoCoordinates
from .location_type import LocationType
from .location_unique_id_type import LocationUniqueIdType

