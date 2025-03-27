from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsCloudPcOverview(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	frontlineLicensesCount: Optional[int] = Field(alias="frontlineLicensesCount", default=None,)
	lastRefreshedDateTime: Optional[datetime] = Field(alias="lastRefreshedDateTime", default=None,)
	numberOfCloudPcConnectionStatusFailed: Optional[int] = Field(alias="numberOfCloudPcConnectionStatusFailed", default=None,)
	numberOfCloudPcConnectionStatusPassed: Optional[int] = Field(alias="numberOfCloudPcConnectionStatusPassed", default=None,)
	numberOfCloudPcConnectionStatusPending: Optional[int] = Field(alias="numberOfCloudPcConnectionStatusPending", default=None,)
	numberOfCloudPcConnectionStatusRunning: Optional[int] = Field(alias="numberOfCloudPcConnectionStatusRunning", default=None,)
	numberOfCloudPcConnectionStatusUnkownFutureValue: Optional[int] = Field(alias="numberOfCloudPcConnectionStatusUnkownFutureValue", default=None,)
	numberOfCloudPcStatusDeprovisioning: Optional[int] = Field(alias="numberOfCloudPcStatusDeprovisioning", default=None,)
	numberOfCloudPcStatusFailed: Optional[int] = Field(alias="numberOfCloudPcStatusFailed", default=None,)
	numberOfCloudPcStatusInGracePeriod: Optional[int] = Field(alias="numberOfCloudPcStatusInGracePeriod", default=None,)
	numberOfCloudPcStatusNotProvisioned: Optional[int] = Field(alias="numberOfCloudPcStatusNotProvisioned", default=None,)
	numberOfCloudPcStatusProvisioned: Optional[int] = Field(alias="numberOfCloudPcStatusProvisioned", default=None,)
	numberOfCloudPcStatusProvisioning: Optional[int] = Field(alias="numberOfCloudPcStatusProvisioning", default=None,)
	numberOfCloudPcStatusUnknown: Optional[int] = Field(alias="numberOfCloudPcStatusUnknown", default=None,)
	numberOfCloudPcStatusUpgrading: Optional[int] = Field(alias="numberOfCloudPcStatusUpgrading", default=None,)
	tenantDisplayName: Optional[str] = Field(alias="tenantDisplayName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	totalBusinessLicenses: Optional[int] = Field(alias="totalBusinessLicenses", default=None,)
	totalCloudPcConnectionStatus: Optional[int] = Field(alias="totalCloudPcConnectionStatus", default=None,)
	totalCloudPcStatus: Optional[int] = Field(alias="totalCloudPcStatus", default=None,)
	totalEnterpriseLicenses: Optional[int] = Field(alias="totalEnterpriseLicenses", default=None,)


