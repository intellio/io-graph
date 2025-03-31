from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsAppPerformance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.appPerformance"] = Field(alias="@odata.type",)
	appFriendlyName: Optional[str] = Field(alias="appFriendlyName", default=None,)
	appName: Optional[str] = Field(alias="appName", default=None,)
	appPublisher: Optional[str] = Field(alias="appPublisher", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	meanTimeToFailureInMinutes: Optional[int] = Field(alias="meanTimeToFailureInMinutes", default=None,)
	tenantDisplayName: Optional[str] = Field(alias="tenantDisplayName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	totalActiveDeviceCount: Optional[int] = Field(alias="totalActiveDeviceCount", default=None,)
	totalAppCrashCount: Optional[int] = Field(alias="totalAppCrashCount", default=None,)
	totalAppFreezeCount: Optional[int] = Field(alias="totalAppFreezeCount", default=None,)

