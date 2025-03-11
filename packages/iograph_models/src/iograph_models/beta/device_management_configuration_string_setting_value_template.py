from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationStringSettingValueTemplate(BaseModel):
	settingValueTemplateId: Optional[str] = Field(alias="settingValueTemplateId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	defaultValue: SerializeAsAny[Optional[DeviceManagementConfigurationStringSettingValueDefaultTemplate]] = Field(alias="defaultValue",default=None,)

from .device_management_configuration_string_setting_value_default_template import DeviceManagementConfigurationStringSettingValueDefaultTemplate

