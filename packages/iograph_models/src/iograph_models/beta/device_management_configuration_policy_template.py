from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationPolicyTemplate(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	allowUnmanagedSettings: Optional[bool] = Field(alias="allowUnmanagedSettings",default=None,)
	baseId: Optional[str] = Field(alias="baseId",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	displayVersion: Optional[str] = Field(alias="displayVersion",default=None,)
	lifecycleState: Optional[DeviceManagementTemplateLifecycleState | str] = Field(alias="lifecycleState",default=None,)
	platforms: Optional[DeviceManagementConfigurationPlatforms | str] = Field(alias="platforms",default=None,)
	settingTemplateCount: Optional[int] = Field(alias="settingTemplateCount",default=None,)
	technologies: Optional[DeviceManagementConfigurationTechnologies | str] = Field(alias="technologies",default=None,)
	templateFamily: Optional[DeviceManagementConfigurationTemplateFamily | str] = Field(alias="templateFamily",default=None,)
	version: Optional[int] = Field(alias="version",default=None,)
	settingTemplates: Optional[list[DeviceManagementConfigurationSettingTemplate]] = Field(alias="settingTemplates",default=None,)

from .device_management_template_lifecycle_state import DeviceManagementTemplateLifecycleState
from .device_management_configuration_platforms import DeviceManagementConfigurationPlatforms
from .device_management_configuration_technologies import DeviceManagementConfigurationTechnologies
from .device_management_configuration_template_family import DeviceManagementConfigurationTemplateFamily
from .device_management_configuration_setting_template import DeviceManagementConfigurationSettingTemplate

