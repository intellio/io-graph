from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagedDeviceComplianceTrendCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ManagedTenantsManagedDeviceComplianceTrend]] = Field(alias="value", default=None,)

from .managed_tenants_managed_device_compliance_trend import ManagedTenantsManagedDeviceComplianceTrend

