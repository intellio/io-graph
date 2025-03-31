from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsDeviceAppPerformance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.deviceAppPerformance"] = Field(alias="@odata.type",)
	appFriendlyName: Optional[str] = Field(alias="appFriendlyName", default=None,)
	appName: Optional[str] = Field(alias="appName", default=None,)
	appPublisher: Optional[str] = Field(alias="appPublisher", default=None,)
	appVersion: Optional[str] = Field(alias="appVersion", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	deviceManufacturer: Optional[str] = Field(alias="deviceManufacturer", default=None,)
	deviceModel: Optional[str] = Field(alias="deviceModel", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	healthStatus: Optional[str] = Field(alias="healthStatus", default=None,)
	isLatestUsedVersion: Optional[int] = Field(alias="isLatestUsedVersion", default=None,)
	isMostUsedVersion: Optional[int] = Field(alias="isMostUsedVersion", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	tenantDisplayName: Optional[str] = Field(alias="tenantDisplayName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	totalAppCrashCount: Optional[int] = Field(alias="totalAppCrashCount", default=None,)
	totalAppFreezeCount: Optional[int] = Field(alias="totalAppFreezeCount", default=None,)

