from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementIntentSettingCategory(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	hasRequiredSetting: Optional[bool] = Field(alias="hasRequiredSetting",default=None,)
	settingDefinitions: SerializeAsAny[Optional[list[DeviceManagementSettingDefinition]]] = Field(alias="settingDefinitions",default=None,)
	settings: SerializeAsAny[Optional[list[DeviceManagementSettingInstance]]] = Field(alias="settings",default=None,)

from .device_management_setting_definition import DeviceManagementSettingDefinition
from .device_management_setting_instance import DeviceManagementSettingInstance

