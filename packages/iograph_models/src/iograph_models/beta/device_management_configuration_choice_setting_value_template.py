from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationChoiceSettingValueTemplate(BaseModel):
	defaultValue: SerializeAsAny[Optional[DeviceManagementConfigurationChoiceSettingValueDefaultTemplate]] = Field(alias="defaultValue",default=None,)
	recommendedValueDefinition: Optional[DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate] = Field(alias="recommendedValueDefinition",default=None,)
	requiredValueDefinition: Optional[DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate] = Field(alias="requiredValueDefinition",default=None,)
	settingValueTemplateId: Optional[str] = Field(alias="settingValueTemplateId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_management_configuration_choice_setting_value_default_template import DeviceManagementConfigurationChoiceSettingValueDefaultTemplate
from .device_management_configuration_choice_setting_value_definition_template import DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate
from .device_management_configuration_choice_setting_value_definition_template import DeviceManagementConfigurationChoiceSettingValueDefinitionTemplate

