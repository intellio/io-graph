from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationGroupSettingInstance(BaseModel):
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId", default=None,)
	settingInstanceTemplateReference: Optional[DeviceManagementConfigurationSettingInstanceTemplateReference] = Field(alias="settingInstanceTemplateReference", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationGroupSettingInstance"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationGroupSettingInstance")
	groupSettingValue: Optional[DeviceManagementConfigurationGroupSettingValue] = Field(alias="groupSettingValue", default=None,)

from .device_management_configuration_setting_instance_template_reference import DeviceManagementConfigurationSettingInstanceTemplateReference
from .device_management_configuration_group_setting_value import DeviceManagementConfigurationGroupSettingValue

