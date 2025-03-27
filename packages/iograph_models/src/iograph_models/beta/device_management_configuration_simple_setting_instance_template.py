from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationSimpleSettingInstanceTemplate(BaseModel):
	isRequired: Optional[bool] = Field(alias="isRequired", default=None,)
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId", default=None,)
	settingInstanceTemplateId: Optional[str] = Field(alias="settingInstanceTemplateId", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationSimpleSettingInstanceTemplate"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationSimpleSettingInstanceTemplate")
	simpleSettingValueTemplate: Optional[Union[DeviceManagementConfigurationIntegerSettingValueTemplate, DeviceManagementConfigurationStringSettingValueTemplate]] = Field(alias="simpleSettingValueTemplate", default=None,discriminator="odata_type", )

from .device_management_configuration_integer_setting_value_template import DeviceManagementConfigurationIntegerSettingValueTemplate
from .device_management_configuration_string_setting_value_template import DeviceManagementConfigurationStringSettingValueTemplate

