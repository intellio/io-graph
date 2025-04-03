from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceConfigurationState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceConfigurationState"] = Field(alias="@odata.type", default="#microsoft.graph.deviceConfigurationState")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	platformType: Optional[PolicyPlatformType | str] = Field(alias="platformType", default=None,)
	settingCount: Optional[int] = Field(alias="settingCount", default=None,)
	settingStates: Optional[list[DeviceConfigurationSettingState]] = Field(alias="settingStates", default=None,)
	state: Optional[ComplianceStatus | str] = Field(alias="state", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)

from .policy_platform_type import PolicyPlatformType
from .device_configuration_setting_state import DeviceConfigurationSettingState
from .compliance_status import ComplianceStatus
