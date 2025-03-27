from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationIntegerSettingValue(BaseModel):
	settingValueTemplateReference: Optional[DeviceManagementConfigurationSettingValueTemplateReference] = Field(alias="settingValueTemplateReference", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationIntegerSettingValue"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationIntegerSettingValue")
	value: Optional[int] = Field(alias="value", default=None,)

from .device_management_configuration_setting_value_template_reference import DeviceManagementConfigurationSettingValueTemplateReference

