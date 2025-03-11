from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationChoiceSettingValueConstantDefaultTemplate(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	children: SerializeAsAny[Optional[list[DeviceManagementConfigurationSettingInstanceTemplate]]] = Field(alias="children",default=None,)
	settingDefinitionOptionId: Optional[str] = Field(alias="settingDefinitionOptionId",default=None,)

from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate

