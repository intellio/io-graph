from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationOptionDefinition(BaseModel):
	dependedOnBy: Optional[list[DeviceManagementConfigurationSettingDependedOnBy]] = Field(alias="dependedOnBy",default=None,)
	dependentOn: Optional[list[DeviceManagementConfigurationDependentOn]] = Field(alias="dependentOn",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	helpText: Optional[str] = Field(alias="helpText",default=None,)
	itemId: Optional[str] = Field(alias="itemId",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	optionValue: SerializeAsAny[Optional[DeviceManagementConfigurationSettingValue]] = Field(alias="optionValue",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_management_configuration_setting_depended_on_by import DeviceManagementConfigurationSettingDependedOnBy
from .device_management_configuration_dependent_on import DeviceManagementConfigurationDependentOn
from .device_management_configuration_setting_value import DeviceManagementConfigurationSettingValue

