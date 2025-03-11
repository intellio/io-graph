from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationSimpleSettingInstanceTemplate(BaseModel):
	isRequired: Optional[bool] = Field(alias="isRequired",default=None,)
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId",default=None,)
	settingInstanceTemplateId: Optional[str] = Field(alias="settingInstanceTemplateId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	simpleSettingValueTemplate: SerializeAsAny[Optional[DeviceManagementConfigurationSimpleSettingValueTemplate]] = Field(alias="simpleSettingValueTemplate",default=None,)

from .device_management_configuration_simple_setting_value_template import DeviceManagementConfigurationSimpleSettingValueTemplate

