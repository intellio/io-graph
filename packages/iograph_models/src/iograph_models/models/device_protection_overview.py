from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceProtectionOverview(BaseModel):
	cleanDeviceCount: Optional[int] = Field(default=None,alias="cleanDeviceCount",)
	criticalFailuresDeviceCount: Optional[int] = Field(default=None,alias="criticalFailuresDeviceCount",)
	inactiveThreatAgentDeviceCount: Optional[int] = Field(default=None,alias="inactiveThreatAgentDeviceCount",)
	pendingFullScanDeviceCount: Optional[int] = Field(default=None,alias="pendingFullScanDeviceCount",)
	pendingManualStepsDeviceCount: Optional[int] = Field(default=None,alias="pendingManualStepsDeviceCount",)
	pendingOfflineScanDeviceCount: Optional[int] = Field(default=None,alias="pendingOfflineScanDeviceCount",)
	pendingQuickScanDeviceCount: Optional[int] = Field(default=None,alias="pendingQuickScanDeviceCount",)
	pendingRestartDeviceCount: Optional[int] = Field(default=None,alias="pendingRestartDeviceCount",)
	pendingSignatureUpdateDeviceCount: Optional[int] = Field(default=None,alias="pendingSignatureUpdateDeviceCount",)
	totalReportedDeviceCount: Optional[int] = Field(default=None,alias="totalReportedDeviceCount",)
	unknownStateThreatAgentDeviceCount: Optional[int] = Field(default=None,alias="unknownStateThreatAgentDeviceCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


