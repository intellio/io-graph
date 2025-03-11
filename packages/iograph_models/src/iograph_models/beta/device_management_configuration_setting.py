from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationSetting(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	settingInstance: SerializeAsAny[Optional[DeviceManagementConfigurationSettingInstance]] = Field(alias="settingInstance",default=None,)
	settingDefinitions: SerializeAsAny[Optional[list[DeviceManagementConfigurationSettingDefinition]]] = Field(alias="settingDefinitions",default=None,)

from .device_management_configuration_setting_instance import DeviceManagementConfigurationSettingInstance
from .device_management_configuration_setting_definition import DeviceManagementConfigurationSettingDefinition

