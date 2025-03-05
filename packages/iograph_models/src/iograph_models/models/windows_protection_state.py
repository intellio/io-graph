from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsProtectionState(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	antiMalwareVersion: Optional[str] = Field(alias="antiMalwareVersion",default=None,)
	deviceState: Optional[str | WindowsDeviceHealthState] = Field(alias="deviceState",default=None,)
	engineVersion: Optional[str] = Field(alias="engineVersion",default=None,)
	fullScanOverdue: Optional[bool] = Field(alias="fullScanOverdue",default=None,)
	fullScanRequired: Optional[bool] = Field(alias="fullScanRequired",default=None,)
	isVirtualMachine: Optional[bool] = Field(alias="isVirtualMachine",default=None,)
	lastFullScanDateTime: Optional[datetime] = Field(alias="lastFullScanDateTime",default=None,)
	lastFullScanSignatureVersion: Optional[str] = Field(alias="lastFullScanSignatureVersion",default=None,)
	lastQuickScanDateTime: Optional[datetime] = Field(alias="lastQuickScanDateTime",default=None,)
	lastQuickScanSignatureVersion: Optional[str] = Field(alias="lastQuickScanSignatureVersion",default=None,)
	lastReportedDateTime: Optional[datetime] = Field(alias="lastReportedDateTime",default=None,)
	malwareProtectionEnabled: Optional[bool] = Field(alias="malwareProtectionEnabled",default=None,)
	networkInspectionSystemEnabled: Optional[bool] = Field(alias="networkInspectionSystemEnabled",default=None,)
	productStatus: Optional[str | WindowsDefenderProductStatus] = Field(alias="productStatus",default=None,)
	quickScanOverdue: Optional[bool] = Field(alias="quickScanOverdue",default=None,)
	realTimeProtectionEnabled: Optional[bool] = Field(alias="realTimeProtectionEnabled",default=None,)
	rebootRequired: Optional[bool] = Field(alias="rebootRequired",default=None,)
	signatureUpdateOverdue: Optional[bool] = Field(alias="signatureUpdateOverdue",default=None,)
	signatureVersion: Optional[str] = Field(alias="signatureVersion",default=None,)
	tamperProtectionEnabled: Optional[bool] = Field(alias="tamperProtectionEnabled",default=None,)
	detectedMalwareState: Optional[list[WindowsDeviceMalwareState]] = Field(alias="detectedMalwareState",default=None,)

from .windows_device_health_state import WindowsDeviceHealthState
from .windows_defender_product_status import WindowsDefenderProductStatus
from .windows_device_malware_state import WindowsDeviceMalwareState

