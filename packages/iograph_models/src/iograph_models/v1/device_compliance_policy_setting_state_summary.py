from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceCompliancePolicySettingStateSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	compliantDeviceCount: Optional[int] = Field(alias="compliantDeviceCount", default=None,)
	conflictDeviceCount: Optional[int] = Field(alias="conflictDeviceCount", default=None,)
	errorDeviceCount: Optional[int] = Field(alias="errorDeviceCount", default=None,)
	nonCompliantDeviceCount: Optional[int] = Field(alias="nonCompliantDeviceCount", default=None,)
	notApplicableDeviceCount: Optional[int] = Field(alias="notApplicableDeviceCount", default=None,)
	platformType: Optional[PolicyPlatformType | str] = Field(alias="platformType", default=None,)
	remediatedDeviceCount: Optional[int] = Field(alias="remediatedDeviceCount", default=None,)
	setting: Optional[str] = Field(alias="setting", default=None,)
	settingName: Optional[str] = Field(alias="settingName", default=None,)
	unknownDeviceCount: Optional[int] = Field(alias="unknownDeviceCount", default=None,)
	deviceComplianceSettingStates: Optional[list[DeviceComplianceSettingState]] = Field(alias="deviceComplianceSettingStates", default=None,)

from .policy_platform_type import PolicyPlatformType
from .device_compliance_setting_state import DeviceComplianceSettingState

