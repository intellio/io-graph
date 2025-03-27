from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkplaceSensorDevice(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	ipV4Address: Optional[str] = Field(alias="ipV4Address", default=None,)
	ipV6Address: Optional[str] = Field(alias="ipV6Address", default=None,)
	macAddress: Optional[str] = Field(alias="macAddress", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	placeId: Optional[str] = Field(alias="placeId", default=None,)
	sensors: Optional[list[WorkplaceSensor]] = Field(alias="sensors", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)

from .workplace_sensor import WorkplaceSensor

