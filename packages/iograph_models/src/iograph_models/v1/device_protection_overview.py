from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceProtectionOverview(BaseModel):
	cleanDeviceCount: Optional[int] = Field(alias="cleanDeviceCount",default=None,)
	criticalFailuresDeviceCount: Optional[int] = Field(alias="criticalFailuresDeviceCount",default=None,)
	inactiveThreatAgentDeviceCount: Optional[int] = Field(alias="inactiveThreatAgentDeviceCount",default=None,)
	pendingFullScanDeviceCount: Optional[int] = Field(alias="pendingFullScanDeviceCount",default=None,)
	pendingManualStepsDeviceCount: Optional[int] = Field(alias="pendingManualStepsDeviceCount",default=None,)
	pendingOfflineScanDeviceCount: Optional[int] = Field(alias="pendingOfflineScanDeviceCount",default=None,)
	pendingQuickScanDeviceCount: Optional[int] = Field(alias="pendingQuickScanDeviceCount",default=None,)
	pendingRestartDeviceCount: Optional[int] = Field(alias="pendingRestartDeviceCount",default=None,)
	pendingSignatureUpdateDeviceCount: Optional[int] = Field(alias="pendingSignatureUpdateDeviceCount",default=None,)
	totalReportedDeviceCount: Optional[int] = Field(alias="totalReportedDeviceCount",default=None,)
	unknownStateThreatAgentDeviceCount: Optional[int] = Field(alias="unknownStateThreatAgentDeviceCount",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


