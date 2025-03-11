from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationSettingTemplate(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	settingInstanceTemplate: SerializeAsAny[Optional[DeviceManagementConfigurationSettingInstanceTemplate]] = Field(alias="settingInstanceTemplate",default=None,)
	settingDefinitions: SerializeAsAny[Optional[list[DeviceManagementConfigurationSettingDefinition]]] = Field(alias="settingDefinitions",default=None,)

from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate
from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition

