from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ManagedDeviceMobileAppConfigurationState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedDeviceMobileAppConfigurationState"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	platformType: Optional[PolicyPlatformType | str] = Field(alias="platformType", default=None,)
	settingCount: Optional[int] = Field(alias="settingCount", default=None,)
	settingStates: Optional[list[ManagedDeviceMobileAppConfigurationSettingState]] = Field(alias="settingStates", default=None,)
	state: Optional[ComplianceStatus | str] = Field(alias="state", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)

from .policy_platform_type import PolicyPlatformType
from .managed_device_mobile_app_configuration_setting_state import ManagedDeviceMobileAppConfigurationSettingState
from .compliance_status import ComplianceStatus
