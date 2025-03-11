from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RoomList(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	address: Optional[PhysicalAddress] = Field(alias="address",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	geoCoordinates: Optional[OutlookGeoCoordinates] = Field(alias="geoCoordinates",default=None,)
	phone: Optional[str] = Field(alias="phone",default=None,)
	placeId: Optional[str] = Field(alias="placeId",default=None,)
	emailAddress: Optional[str] = Field(alias="emailAddress",default=None,)
	rooms: Optional[list[Room]] = Field(alias="rooms",default=None,)
	workspaces: Optional[list[Workspace]] = Field(alias="workspaces",default=None,)

from .physical_address import PhysicalAddress
from .outlook_geo_coordinates import OutlookGeoCoordinates
from .room import Room
from .workspace import Workspace

