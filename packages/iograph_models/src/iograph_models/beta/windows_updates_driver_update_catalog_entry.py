from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsUpdatesDriverUpdateCatalogEntry(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsUpdates.driverUpdateCatalogEntry"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdates.driverUpdateCatalogEntry")
	deployableUntilDateTime: Optional[datetime] = Field(alias="deployableUntilDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	releaseDateTime: Optional[datetime] = Field(alias="releaseDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	driverClass: Optional[str] = Field(alias="driverClass", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	provider: Optional[str] = Field(alias="provider", default=None,)
	setupInformationFile: Optional[str] = Field(alias="setupInformationFile", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	versionDateTime: Optional[datetime] = Field(alias="versionDateTime", default=None,)

