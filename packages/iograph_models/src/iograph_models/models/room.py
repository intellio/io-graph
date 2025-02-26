from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Room(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	address: Optional[PhysicalAddress] = Field(default=None,alias="address",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	geoCoordinates: Optional[OutlookGeoCoordinates] = Field(default=None,alias="geoCoordinates",)
	phone: Optional[str] = Field(default=None,alias="phone",)
	audioDeviceName: Optional[str] = Field(default=None,alias="audioDeviceName",)
	bookingType: Optional[BookingType] = Field(default=None,alias="bookingType",)
	building: Optional[str] = Field(default=None,alias="building",)
	capacity: Optional[int] = Field(default=None,alias="capacity",)
	displayDeviceName: Optional[str] = Field(default=None,alias="displayDeviceName",)
	emailAddress: Optional[str] = Field(default=None,alias="emailAddress",)
	floorLabel: Optional[str] = Field(default=None,alias="floorLabel",)
	floorNumber: Optional[int] = Field(default=None,alias="floorNumber",)
	isWheelChairAccessible: Optional[bool] = Field(default=None,alias="isWheelChairAccessible",)
	label: Optional[str] = Field(default=None,alias="label",)
	nickname: Optional[str] = Field(default=None,alias="nickname",)
	tags: list[Optional[str]] = Field(alias="tags",)
	videoDeviceName: Optional[str] = Field(default=None,alias="videoDeviceName",)

from .physical_address import PhysicalAddress
from .outlook_geo_coordinates import OutlookGeoCoordinates
from .booking_type import BookingType

