from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationSimpleSettingCollectionInstanceTemplate(BaseModel):
	isRequired: Optional[bool] = Field(alias="isRequired", default=None,)
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId", default=None,)
	settingInstanceTemplateId: Optional[str] = Field(alias="settingInstanceTemplateId", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionInstanceTemplate"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationSimpleSettingCollectionInstanceTemplate")
	allowUnmanagedValues: Optional[bool] = Field(alias="allowUnmanagedValues", default=None,)
	simpleSettingCollectionValueTemplate: Optional[list[Annotated[Union[DeviceManagementConfigurationIntegerSettingValueTemplate, DeviceManagementConfigurationStringSettingValueTemplate]],Field(discriminator="odata_type")]]] = Field(alias="simpleSettingCollectionValueTemplate", default=None,)

from .device_management_configuration_integer_setting_value_template import DeviceManagementConfigurationIntegerSettingValueTemplate
from .device_management_configuration_string_setting_value_template import DeviceManagementConfigurationStringSettingValueTemplate

