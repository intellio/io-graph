from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationOptionDefinitionTemplate(BaseModel):
	children: SerializeAsAny[Optional[list[DeviceManagementConfigurationSettingInstanceTemplate]]] = Field(alias="children",default=None,)
	itemId: Optional[str] = Field(alias="itemId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_management_configuration_setting_instance_template import DeviceManagementConfigurationSettingInstanceTemplate

