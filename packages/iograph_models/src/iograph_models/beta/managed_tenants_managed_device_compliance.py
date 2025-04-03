from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsManagedDeviceCompliance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.managedDeviceCompliance"] = Field(alias="@odata.type", default="#microsoft.graph.managedTenants.managedDeviceCompliance")
	complianceStatus: Optional[str] = Field(alias="complianceStatus", default=None,)
	deviceType: Optional[str] = Field(alias="deviceType", default=None,)
	inGracePeriodUntilDateTime: Optional[datetime] = Field(alias="inGracePeriodUntilDateTime", default=None,)
	lastRefreshedDateTime: Optional[datetime] = Field(alias="lastRefreshedDateTime", default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime", default=None,)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId", default=None,)
	managedDeviceName: Optional[str] = Field(alias="managedDeviceName", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	osDescription: Optional[str] = Field(alias="osDescription", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	ownerType: Optional[str] = Field(alias="ownerType", default=None,)
	tenantDisplayName: Optional[str] = Field(alias="tenantDisplayName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)

