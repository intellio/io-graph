from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementConfigurationReferenceSettingValue(BaseModel):
	settingValueTemplateReference: Optional[DeviceManagementConfigurationSettingValueTemplateReference] = Field(alias="settingValueTemplateReference", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementConfigurationReferenceSettingValue"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementConfigurationReferenceSettingValue")
	value: Optional[str] = Field(alias="value", default=None,)
	note: Optional[str] = Field(alias="note", default=None,)

from .device_management_configuration_setting_value_template_reference import DeviceManagementConfigurationSettingValueTemplateReference
