from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationChoiceSettingInstanceTemplate(BaseModel):
	isRequired: Optional[bool] = Field(alias="isRequired",default=None,)
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId",default=None,)
	settingInstanceTemplateId: Optional[str] = Field(alias="settingInstanceTemplateId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	choiceSettingValueTemplate: Optional[DeviceManagementConfigurationChoiceSettingValueTemplate] = Field(alias="choiceSettingValueTemplate",default=None,)

from .device_management_configuration_choice_setting_value_template import DeviceManagementConfigurationChoiceSettingValueTemplate

