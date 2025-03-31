from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedTenantsCloudPcDeviceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ManagedTenantsCloudPcDevice]] = Field(alias="value", default=None,)

from .managed_tenants_cloud_pc_device import ManagedTenantsCloudPcDevice
