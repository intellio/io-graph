from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceManagementConfigurationChoiceSettingValueCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DeviceManagementConfigurationChoiceSettingValue]] = Field(alias="value", default=None,)

from .device_management_configuration_choice_setting_value import DeviceManagementConfigurationChoiceSettingValue
