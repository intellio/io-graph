from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RoomList(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	address: Optional[PhysicalAddress] = Field(default=None,alias="address",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	geoCoordinates: Optional[OutlookGeoCoordinates] = Field(default=None,alias="geoCoordinates",)
	phone: Optional[str] = Field(default=None,alias="phone",)
	emailAddress: Optional[str] = Field(default=None,alias="emailAddress",)
	rooms: Optional[list[Room]] = Field(default=None,alias="rooms",)

from .physical_address import PhysicalAddress
from .outlook_geo_coordinates import OutlookGeoCoordinates
from .room import Room

