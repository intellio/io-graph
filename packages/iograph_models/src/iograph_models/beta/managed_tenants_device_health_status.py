from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsDeviceHealthStatus(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.deviceHealthStatus"] = Field(alias="@odata.type",)
	blueScreenCount: Optional[int] = Field(alias="blueScreenCount", default=None,)
	bootTotalDurationInSeconds: float | str | ReferenceNumeric
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	deviceMake: Optional[str] = Field(alias="deviceMake", default=None,)
	deviceModel: Optional[str] = Field(alias="deviceModel", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	healthStatus: Optional[str] = Field(alias="healthStatus", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	primaryDiskType: Optional[str] = Field(alias="primaryDiskType", default=None,)
	restartCount: Optional[int] = Field(alias="restartCount", default=None,)
	startupPerformanceScore: float | str | ReferenceNumeric
	tenantDisplayName: Optional[str] = Field(alias="tenantDisplayName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	topProcesses: Optional[str] = Field(alias="topProcesses", default=None,)

from .reference_numeric import ReferenceNumeric
