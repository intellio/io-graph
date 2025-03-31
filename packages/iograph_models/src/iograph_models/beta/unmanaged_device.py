from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UnmanagedDevice(BaseModel):
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	domain: Optional[str] = Field(alias="domain", default=None,)
	ipAddress: Optional[str] = Field(alias="ipAddress", default=None,)
	lastLoggedOnUser: Optional[str] = Field(alias="lastLoggedOnUser", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	location: Optional[str] = Field(alias="location", default=None,)
	macAddress: Optional[str] = Field(alias="macAddress", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	os: Optional[str] = Field(alias="os", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

