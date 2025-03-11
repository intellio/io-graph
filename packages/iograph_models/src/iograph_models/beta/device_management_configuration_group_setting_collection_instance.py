from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementConfigurationGroupSettingCollectionInstance(BaseModel):
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId",default=None,)
	settingInstanceTemplateReference: Optional[DeviceManagementConfigurationSettingInstanceTemplateReference] = Field(alias="settingInstanceTemplateReference",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	groupSettingCollectionValue: Optional[list[DeviceManagementConfigurationGroupSettingValue]] = Field(alias="groupSettingCollectionValue",default=None,)

from .device_management_configuration_setting_instance_template_reference import DeviceManagementConfigurationSettingInstanceTemplateReference
from .device_management_configuration_group_setting_value import DeviceManagementConfigurationGroupSettingValue

