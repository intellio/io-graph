from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementConfigurationChoiceSettingInstance(BaseModel):
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId", default=None,)
	settingInstanceTemplateReference: Optional[DeviceManagementConfigurationSettingInstanceTemplateReference] = Field(alias="settingInstanceTemplateReference", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationChoiceSettingInstance"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationChoiceSettingInstance")
	choiceSettingValue: Optional[DeviceManagementConfigurationChoiceSettingValue] = Field(alias="choiceSettingValue", default=None,)

from .device_management_configuration_setting_instance_template_reference import DeviceManagementConfigurationSettingInstanceTemplateReference
from .device_management_configuration_choice_setting_value import DeviceManagementConfigurationChoiceSettingValue
