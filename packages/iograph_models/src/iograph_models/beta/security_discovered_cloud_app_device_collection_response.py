from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityDiscoveredCloudAppDeviceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityDiscoveredCloudAppDevice]] = Field(alias="value", default=None,)

from .security_discovered_cloud_app_device import SecurityDiscoveredCloudAppDevice
