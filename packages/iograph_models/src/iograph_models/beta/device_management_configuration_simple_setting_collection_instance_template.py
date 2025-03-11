from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationSimpleSettingCollectionInstanceTemplate(BaseModel):
	isRequired: Optional[bool] = Field(alias="isRequired",default=None,)
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId",default=None,)
	settingInstanceTemplateId: Optional[str] = Field(alias="settingInstanceTemplateId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	allowUnmanagedValues: Optional[bool] = Field(alias="allowUnmanagedValues",default=None,)
	simpleSettingCollectionValueTemplate: SerializeAsAny[Optional[list[DeviceManagementConfigurationSimpleSettingValueTemplate]]] = Field(alias="simpleSettingCollectionValueTemplate",default=None,)

from .device_management_configuration_simple_setting_value_template import DeviceManagementConfigurationSimpleSettingValueTemplate

