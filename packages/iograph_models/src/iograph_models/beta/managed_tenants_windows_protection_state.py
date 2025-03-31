from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsWindowsProtectionState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.windowsProtectionState"] = Field(alias="@odata.type",)
	antiMalwareVersion: Optional[str] = Field(alias="antiMalwareVersion", default=None,)
	attentionRequired: Optional[bool] = Field(alias="attentionRequired", default=None,)
	deviceDeleted: Optional[bool] = Field(alias="deviceDeleted", default=None,)
	devicePropertyRefreshDateTime: Optional[datetime] = Field(alias="devicePropertyRefreshDateTime", default=None,)
	engineVersion: Optional[str] = Field(alias="engineVersion", default=None,)
	fullScanOverdue: Optional[bool] = Field(alias="fullScanOverdue", default=None,)
	fullScanRequired: Optional[bool] = Field(alias="fullScanRequired", default=None,)
	lastFullScanDateTime: Optional[datetime] = Field(alias="lastFullScanDateTime", default=None,)
	lastFullScanSignatureVersion: Optional[str] = Field(alias="lastFullScanSignatureVersion", default=None,)
	lastQuickScanDateTime: Optional[datetime] = Field(alias="lastQuickScanDateTime", default=None,)
	lastQuickScanSignatureVersion: Optional[str] = Field(alias="lastQuickScanSignatureVersion", default=None,)
	lastRefreshedDateTime: Optional[datetime] = Field(alias="lastRefreshedDateTime", default=None,)
	lastReportedDateTime: Optional[datetime] = Field(alias="lastReportedDateTime", default=None,)
	malwareProtectionEnabled: Optional[bool] = Field(alias="malwareProtectionEnabled", default=None,)
	managedDeviceHealthState: Optional[str] = Field(alias="managedDeviceHealthState", default=None,)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId", default=None,)
	managedDeviceName: Optional[str] = Field(alias="managedDeviceName", default=None,)
	networkInspectionSystemEnabled: Optional[bool] = Field(alias="networkInspectionSystemEnabled", default=None,)
	quickScanOverdue: Optional[bool] = Field(alias="quickScanOverdue", default=None,)
	realTimeProtectionEnabled: Optional[bool] = Field(alias="realTimeProtectionEnabled", default=None,)
	rebootRequired: Optional[bool] = Field(alias="rebootRequired", default=None,)
	signatureUpdateOverdue: Optional[bool] = Field(alias="signatureUpdateOverdue", default=None,)
	signatureVersion: Optional[str] = Field(alias="signatureVersion", default=None,)
	tenantDisplayName: Optional[str] = Field(alias="tenantDisplayName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)

