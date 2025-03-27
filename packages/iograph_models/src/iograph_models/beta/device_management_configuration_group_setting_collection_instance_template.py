from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationGroupSettingCollectionInstanceTemplate(BaseModel):
	isRequired: Optional[bool] = Field(alias="isRequired", default=None,)
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId", default=None,)
	settingInstanceTemplateId: Optional[str] = Field(alias="settingInstanceTemplateId", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationGroupSettingCollectionInstanceTemplate"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationGroupSettingCollectionInstanceTemplate")
	allowUnmanagedValues: Optional[bool] = Field(alias="allowUnmanagedValues", default=None,)
	groupSettingCollectionValueTemplate: Optional[list[DeviceManagementConfigurationGroupSettingValueTemplate]] = Field(alias="groupSettingCollectionValueTemplate", default=None,)

from .device_management_configuration_group_setting_value_template import DeviceManagementConfigurationGroupSettingValueTemplate

