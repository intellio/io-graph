from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceManagementConfigurationPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationPolicy")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	creationSource: Optional[str] = Field(alias="creationSource", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	isAssigned: Optional[bool] = Field(alias="isAssigned", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	platforms: Optional[DeviceManagementConfigurationPlatforms | str] = Field(alias="platforms", default=None,)
	priorityMetaData: Optional[DeviceManagementPriorityMetaData] = Field(alias="priorityMetaData", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	settingCount: Optional[int] = Field(alias="settingCount", default=None,)
	technologies: Optional[DeviceManagementConfigurationTechnologies | str] = Field(alias="technologies", default=None,)
	templateReference: Optional[DeviceManagementConfigurationPolicyTemplateReference] = Field(alias="templateReference", default=None,)
	assignments: Optional[list[DeviceManagementConfigurationPolicyAssignment]] = Field(alias="assignments", default=None,)
	settings: Optional[list[DeviceManagementConfigurationSetting]] = Field(alias="settings", default=None,)

from .device_management_configuration_platforms import DeviceManagementConfigurationPlatforms
from .device_management_priority_meta_data import DeviceManagementPriorityMetaData
from .device_management_configuration_technologies import DeviceManagementConfigurationTechnologies
from .device_management_configuration_policy_template_reference import DeviceManagementConfigurationPolicyTemplateReference
from .device_management_configuration_policy_assignment import DeviceManagementConfigurationPolicyAssignment
from .device_management_configuration_setting import DeviceManagementConfigurationSetting
