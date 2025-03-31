from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class PrintConnector(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.printConnector"] = Field(alias="@odata.type",)
	appVersion: Optional[str] = Field(alias="appVersion", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	fullyQualifiedDomainName: Optional[str] = Field(alias="fullyQualifiedDomainName", default=None,)
	location: Optional[PrinterLocation] = Field(alias="location", default=None,)
	operatingSystem: Optional[str] = Field(alias="operatingSystem", default=None,)
	registeredDateTime: Optional[datetime] = Field(alias="registeredDateTime", default=None,)

from .printer_location import PrinterLocation
