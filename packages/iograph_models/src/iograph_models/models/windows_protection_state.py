from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsProtectionState(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	antiMalwareVersion: Optional[str] = Field(default=None,alias="antiMalwareVersion",)
	deviceState: Optional[WindowsDeviceHealthState] = Field(default=None,alias="deviceState",)
	engineVersion: Optional[str] = Field(default=None,alias="engineVersion",)
	fullScanOverdue: Optional[bool] = Field(default=None,alias="fullScanOverdue",)
	fullScanRequired: Optional[bool] = Field(default=None,alias="fullScanRequired",)
	isVirtualMachine: Optional[bool] = Field(default=None,alias="isVirtualMachine",)
	lastFullScanDateTime: Optional[datetime] = Field(default=None,alias="lastFullScanDateTime",)
	lastFullScanSignatureVersion: Optional[str] = Field(default=None,alias="lastFullScanSignatureVersion",)
	lastQuickScanDateTime: Optional[datetime] = Field(default=None,alias="lastQuickScanDateTime",)
	lastQuickScanSignatureVersion: Optional[str] = Field(default=None,alias="lastQuickScanSignatureVersion",)
	lastReportedDateTime: Optional[datetime] = Field(default=None,alias="lastReportedDateTime",)
	malwareProtectionEnabled: Optional[bool] = Field(default=None,alias="malwareProtectionEnabled",)
	networkInspectionSystemEnabled: Optional[bool] = Field(default=None,alias="networkInspectionSystemEnabled",)
	productStatus: Optional[WindowsDefenderProductStatus] = Field(default=None,alias="productStatus",)
	quickScanOverdue: Optional[bool] = Field(default=None,alias="quickScanOverdue",)
	realTimeProtectionEnabled: Optional[bool] = Field(default=None,alias="realTimeProtectionEnabled",)
	rebootRequired: Optional[bool] = Field(default=None,alias="rebootRequired",)
	signatureUpdateOverdue: Optional[bool] = Field(default=None,alias="signatureUpdateOverdue",)
	signatureVersion: Optional[str] = Field(default=None,alias="signatureVersion",)
	tamperProtectionEnabled: Optional[bool] = Field(default=None,alias="tamperProtectionEnabled",)
	detectedMalwareState: Optional[list[WindowsDeviceMalwareState]] = Field(default=None,alias="detectedMalwareState",)

from .windows_device_health_state import WindowsDeviceHealthState
from .windows_defender_product_status import WindowsDefenderProductStatus
from .windows_device_malware_state import WindowsDeviceMalwareState

