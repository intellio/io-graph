from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementConfigurationChoiceSettingCollectionInstance(BaseModel):
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId", default=None,)
	settingInstanceTemplateReference: Optional[DeviceManagementConfigurationSettingInstanceTemplateReference] = Field(alias="settingInstanceTemplateReference", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationChoiceSettingCollectionInstance"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationChoiceSettingCollectionInstance")
	choiceSettingCollectionValue: Optional[list[DeviceManagementConfigurationChoiceSettingValue]] = Field(alias="choiceSettingCollectionValue", default=None,)

from .device_management_configuration_setting_instance_template_reference import DeviceManagementConfigurationSettingInstanceTemplateReference
from .device_management_configuration_choice_setting_value import DeviceManagementConfigurationChoiceSettingValue
