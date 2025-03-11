from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationIntegerSettingValueTemplate(BaseModel):
	settingValueTemplateId: Optional[str] = Field(alias="settingValueTemplateId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	defaultValue: SerializeAsAny[Optional[DeviceManagementConfigurationIntegerSettingValueDefaultTemplate]] = Field(alias="defaultValue",default=None,)
	recommendedValueDefinition: Optional[DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate] = Field(alias="recommendedValueDefinition",default=None,)
	requiredValueDefinition: Optional[DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate] = Field(alias="requiredValueDefinition",default=None,)

from .device_management_configuration_integer_setting_value_default_template import DeviceManagementConfigurationIntegerSettingValueDefaultTemplate
from .device_management_configuration_integer_setting_value_definition_template import DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate
from .device_management_configuration_integer_setting_value_definition_template import DeviceManagementConfigurationIntegerSettingValueDefinitionTemplate

