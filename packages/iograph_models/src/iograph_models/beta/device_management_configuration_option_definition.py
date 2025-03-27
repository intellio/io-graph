from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationOptionDefinition(BaseModel):
	dependedOnBy: Optional[list[DeviceManagementConfigurationSettingDependedOnBy]] = Field(alias="dependedOnBy", default=None,)
	dependentOn: Optional[list[DeviceManagementConfigurationDependentOn]] = Field(alias="dependentOn", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	helpText: Optional[str] = Field(alias="helpText", default=None,)
	itemId: Optional[str] = Field(alias="itemId", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	optionValue: Optional[Union[DeviceManagementConfigurationChoiceSettingValue, DeviceManagementConfigurationGroupSettingValue, DeviceManagementConfigurationSimpleSettingValue, DeviceManagementConfigurationIntegerSettingValue, DeviceManagementConfigurationSecretSettingValue, DeviceManagementConfigurationStringSettingValue, DeviceManagementConfigurationReferenceSettingValue]] = Field(alias="optionValue", default=None,discriminator="odata_type", )
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_management_configuration_setting_depended_on_by import DeviceManagementConfigurationSettingDependedOnBy
from .device_management_configuration_dependent_on import DeviceManagementConfigurationDependentOn
from .device_management_configuration_choice_setting_value import DeviceManagementConfigurationChoiceSettingValue
from .device_management_configuration_group_setting_value import DeviceManagementConfigurationGroupSettingValue
from .device_management_configuration_simple_setting_value import DeviceManagementConfigurationSimpleSettingValue
from .device_management_configuration_integer_setting_value import DeviceManagementConfigurationIntegerSettingValue
from .device_management_configuration_secret_setting_value import DeviceManagementConfigurationSecretSettingValue
from .device_management_configuration_string_setting_value import DeviceManagementConfigurationStringSettingValue
from .device_management_configuration_reference_setting_value import DeviceManagementConfigurationReferenceSettingValue

