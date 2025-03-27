from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsCloudPcOverviewCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ManagedTenantsCloudPcOverview]] = Field(alias="value", default=None,)

from .managed_tenants_cloud_pc_overview import ManagedTenantsCloudPcOverview

