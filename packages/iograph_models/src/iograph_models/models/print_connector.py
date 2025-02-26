from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PrintConnector(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appVersion: Optional[str] = Field(default=None,alias="appVersion",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	fullyQualifiedDomainName: Optional[str] = Field(default=None,alias="fullyQualifiedDomainName",)
	location: Optional[PrinterLocation] = Field(default=None,alias="location",)
	operatingSystem: Optional[str] = Field(default=None,alias="operatingSystem",)
	registeredDateTime: Optional[datetime] = Field(default=None,alias="registeredDateTime",)

from .printer_location import PrinterLocation

