from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesFeatureUpdateCatalogEntry(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsUpdates.featureUpdateCatalogEntry"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdates.featureUpdateCatalogEntry")
	deployableUntilDateTime: Optional[datetime] = Field(alias="deployableUntilDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	releaseDateTime: Optional[datetime] = Field(alias="releaseDateTime", default=None,)
	buildNumber: Optional[str] = Field(alias="buildNumber", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)


