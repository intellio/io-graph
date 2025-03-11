from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingInsightsDefinition(BaseModel):
	settingDefinitionId: Optional[str] = Field(alias="settingDefinitionId",default=None,)
	settingInsight: SerializeAsAny[Optional[DeviceManagementConfigurationSettingValue]] = Field(alias="settingInsight",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_management_configuration_setting_value import DeviceManagementConfigurationSettingValue

