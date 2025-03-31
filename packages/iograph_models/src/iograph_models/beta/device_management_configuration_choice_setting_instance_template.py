from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementConfigurationChoiceSettingInstanceTemplate(BaseModel):
	isRequired: Optional[bool] = Field(alias="isRequired", default=None,)
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId", default=None,)
	settingInstanceTemplateId: Optional[str] = Field(alias="settingInstanceTemplateId", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationChoiceSettingInstanceTemplate"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationChoiceSettingInstanceTemplate")
	choiceSettingValueTemplate: Optional[DeviceManagementConfigurationChoiceSettingValueTemplate] = Field(alias="choiceSettingValueTemplate", default=None,)

from .device_management_configuration_choice_setting_value_template import DeviceManagementConfigurationChoiceSettingValueTemplate
