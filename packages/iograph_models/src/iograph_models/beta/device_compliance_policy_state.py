from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceCompliancePolicyState(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	platformType: Optional[PolicyPlatformType | str] = Field(alias="platformType",default=None,)
	settingCount: Optional[int] = Field(alias="settingCount",default=None,)
	settingStates: Optional[list[DeviceCompliancePolicySettingState]] = Field(alias="settingStates",default=None,)
	state: Optional[ComplianceStatus | str] = Field(alias="state",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)

from .policy_platform_type import PolicyPlatformType
from .device_compliance_policy_setting_state import DeviceCompliancePolicySettingState
from .compliance_status import ComplianceStatus

