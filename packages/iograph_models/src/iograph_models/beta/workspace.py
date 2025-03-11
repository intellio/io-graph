from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Workspace(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	address: Optional[PhysicalAddress] = Field(alias="address",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	geoCoordinates: Optional[OutlookGeoCoordinates] = Field(alias="geoCoordinates",default=None,)
	phone: Optional[str] = Field(alias="phone",default=None,)
	placeId: Optional[str] = Field(alias="placeId",default=None,)
	building: Optional[str] = Field(alias="building",default=None,)
	capacity: Optional[int] = Field(alias="capacity",default=None,)
	emailAddress: Optional[str] = Field(alias="emailAddress",default=None,)
	floorLabel: Optional[str] = Field(alias="floorLabel",default=None,)
	floorNumber: Optional[int] = Field(alias="floorNumber",default=None,)
	isWheelChairAccessible: Optional[bool] = Field(alias="isWheelChairAccessible",default=None,)
	label: Optional[str] = Field(alias="label",default=None,)
	nickname: Optional[str] = Field(alias="nickname",default=None,)
	tags: Optional[list[str]] = Field(alias="tags",default=None,)

from .physical_address import PhysicalAddress
from .outlook_geo_coordinates import OutlookGeoCoordinates

