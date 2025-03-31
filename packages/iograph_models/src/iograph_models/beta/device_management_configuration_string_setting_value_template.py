from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementConfigurationStringSettingValueTemplate(BaseModel):
	settingValueTemplateId: Optional[str] = Field(alias="settingValueTemplateId", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationStringSettingValueTemplate"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationStringSettingValueTemplate")
	defaultValue: Optional[Union[DeviceManagementConfigurationStringSettingValueConstantDefaultTemplate]] = Field(alias="defaultValue", default=None,discriminator="odata_type", )

from .device_management_configuration_string_setting_value_constant_default_template import DeviceManagementConfigurationStringSettingValueConstantDefaultTemplate
