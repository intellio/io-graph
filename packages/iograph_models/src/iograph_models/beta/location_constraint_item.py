from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class LocationConstraintItem(BaseModel):
	address: Optional[PhysicalAddress] = Field(alias="address", default=None,)
	coordinates: Optional[OutlookGeoCoordinates] = Field(alias="coordinates", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	locationEmailAddress: Optional[str] = Field(alias="locationEmailAddress", default=None,)
	locationType: Optional[LocationType | str] = Field(alias="locationType", default=None,)
	locationUri: Optional[str] = Field(alias="locationUri", default=None,)
	uniqueId: Optional[str] = Field(alias="uniqueId", default=None,)
	uniqueIdType: Optional[LocationUniqueIdType | str] = Field(alias="uniqueIdType", default=None,)
	odata_type: Literal["#microsoft.graph.locationConstraintItem"] = Field(alias="@odata.type", default="#microsoft.graph.locationConstraintItem")
	resolveAvailability: Optional[bool] = Field(alias="resolveAvailability", default=None,)

from .physical_address import PhysicalAddress
from .outlook_geo_coordinates import OutlookGeoCoordinates
from .location_type import LocationType
from .location_unique_id_type import LocationUniqueIdType
