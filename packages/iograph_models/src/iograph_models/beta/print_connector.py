from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PrintConnector(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	appVersion: Optional[str] = Field(alias="appVersion", default=None,)
	deviceHealth: Optional[DeviceHealth] = Field(alias="deviceHealth", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	fullyQualifiedDomainName: Optional[str] = Field(alias="fullyQualifiedDomainName", default=None,)
	location: Optional[PrinterLocation] = Field(alias="location", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	operatingSystem: Optional[str] = Field(alias="operatingSystem", default=None,)
	registeredDateTime: Optional[datetime] = Field(alias="registeredDateTime", default=None,)

from .device_health import DeviceHealth
from .printer_location import PrinterLocation

