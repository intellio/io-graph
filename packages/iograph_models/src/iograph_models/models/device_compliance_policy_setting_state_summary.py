from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceCompliancePolicySettingStateSummary(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	compliantDeviceCount: Optional[int] = Field(default=None,alias="compliantDeviceCount",)
	conflictDeviceCount: Optional[int] = Field(default=None,alias="conflictDeviceCount",)
	errorDeviceCount: Optional[int] = Field(default=None,alias="errorDeviceCount",)
	nonCompliantDeviceCount: Optional[int] = Field(default=None,alias="nonCompliantDeviceCount",)
	notApplicableDeviceCount: Optional[int] = Field(default=None,alias="notApplicableDeviceCount",)
	platformType: Optional[PolicyPlatformType] = Field(default=None,alias="platformType",)
	remediatedDeviceCount: Optional[int] = Field(default=None,alias="remediatedDeviceCount",)
	setting: Optional[str] = Field(default=None,alias="setting",)
	settingName: Optional[str] = Field(default=None,alias="settingName",)
	unknownDeviceCount: Optional[int] = Field(default=None,alias="unknownDeviceCount",)
	deviceComplianceSettingStates: list[DeviceComplianceSettingState] = Field(alias="deviceComplianceSettingStates",)

from .policy_platform_type import PolicyPlatformType
from .device_compliance_setting_state import DeviceComplianceSettingState

