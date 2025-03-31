from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementConfigurationIntegerSettingValueTemplate(BaseModel):
	settingValueTemplateId: Optional[str] = Field(alias="settingValueTemplateId", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationIntegerSettingValueTemplate"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationIntegerSettingValueTemplate")
	defaultValue: Optional[Union[DeviceManagementConfigurationIntegerSettingValueConstantDefaultTemplate]] = Field(alias="defaultValue", default=None,discriminator="odata_type", )
	recommendedValueDefinition: Optional[DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate] = Field(alias="recommendedValueDefinition", default=None,)
	requiredValueDefinition: Optional[DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate] = Field(alias="requiredValueDefinition", default=None,)

from .device_management_configuration_integer_setting_value_constant_default_template import DeviceManagementConfigurationIntegerSettingValueConstantDefaultTemplate
from .device_management_configuration_integer_setting_value_definition_template import DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate
