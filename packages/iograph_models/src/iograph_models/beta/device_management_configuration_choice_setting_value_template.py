from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class DeviceManagementConfigurationChoiceSettingValueTemplate(BaseModel):
	defaultValue: Optional[Union[DeviceManagementConfigurationChoiceSettingValueConstantDefaultTemplate]] = Field(alias="defaultValue", default=None,discriminator="odata_type", )
	recommendedValueDefinition: Optional[DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate] = Field(alias="recommendedValueDefinition", default=None,)
	requiredValueDefinition: Optional[DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate] = Field(alias="requiredValueDefinition", default=None,)
	settingValueTemplateId: Optional[str] = Field(alias="settingValueTemplateId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_management_configuration_choice_setting_value_constant_default_template import DeviceManagementConfigurationChoiceSettingValueConstantDefaultTemplate
from .device_management_configuration_choice_setting_value_definition_template import DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate
