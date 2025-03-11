from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationChoiceSettingCollectionInstance(BaseModel):
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId",default=None,)
	settingInstanceTemplateReference: Optional[DeviceManagementConfigurationSettingInstanceTemplateReference] = Field(alias="settingInstanceTemplateReference",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	choiceSettingCollectionValue: Optional[list[DeviceManagementConfigurationChoiceSettingValue]] = Field(alias="choiceSettingCollectionValue",default=None,)

from .device_management_configuration_setting_instance_template_reference import DeviceManagementConfigurationSettingInstanceTemplateReference
from .device_management_configuration_choice_setting_value import DeviceManagementConfigurationChoiceSettingValue

