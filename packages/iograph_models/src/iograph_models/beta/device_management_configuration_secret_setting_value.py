from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationSecretSettingValue(BaseModel):
	settingValueTemplateReference: Optional[DeviceManagementConfigurationSettingValueTemplateReference] = Field(alias="settingValueTemplateReference",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	value: Optional[str] = Field(alias="value",default=None,)
	valueState: Optional[DeviceManagementConfigurationSecretSettingValueState | str] = Field(alias="valueState",default=None,)

from .device_management_configuration_setting_value_template_reference import DeviceManagementConfigurationSettingValueTemplateReference
from .device_management_configuration_secret_setting_value_state import DeviceManagementConfigurationSecretSettingValueState

