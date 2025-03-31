from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceManagementCompliancePolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementCompliancePolicy"] = Field(alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	creationSource: Optional[str] = Field(alias="creationSource", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	isAssigned: Optional[bool] = Field(alias="isAssigned", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	platforms: Optional[DeviceManagementConfigurationPlatforms | str] = Field(alias="platforms", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	settingCount: Optional[int] = Field(alias="settingCount", default=None,)
	technologies: Optional[DeviceManagementConfigurationTechnologies | str] = Field(alias="technologies", default=None,)
	assignments: Optional[list[DeviceManagementConfigurationPolicyAssignment]] = Field(alias="assignments", default=None,)
	scheduledActionsForRule: Optional[list[DeviceManagementComplianceScheduledActionForRule]] = Field(alias="scheduledActionsForRule", default=None,)
	settings: Optional[list[DeviceManagementConfigurationSetting]] = Field(alias="settings", default=None,)

from .device_management_configuration_platforms import DeviceManagementConfigurationPlatforms
from .device_management_configuration_technologies import DeviceManagementConfigurationTechnologies
from .device_management_configuration_policy_assignment import DeviceManagementConfigurationPolicyAssignment
from .device_management_compliance_scheduled_action_for_rule import DeviceManagementComplianceScheduledActionForRule
from .device_management_configuration_setting import DeviceManagementConfigurationSetting
