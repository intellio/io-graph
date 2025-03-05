from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceCompliancePolicyState(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	platformType: Optional[PolicyPlatformType] = Field(default=None,alias="platformType",)
	settingCount: Optional[int] = Field(default=None,alias="settingCount",)
	settingStates: Optional[list[DeviceCompliancePolicySettingState]] = Field(default=None,alias="settingStates",)
	state: Optional[ComplianceStatus] = Field(default=None,alias="state",)
	version: Optional[int] = Field(default=None,alias="version",)

from .policy_platform_type import PolicyPlatformType
from .device_compliance_policy_setting_state import DeviceCompliancePolicySettingState
from .compliance_status import ComplianceStatus

