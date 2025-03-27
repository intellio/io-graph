from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Change_settingsPostRequest(BaseModel):
	settings: Optional[list[DeviceManagementConfigurationSetting]] = Field(alias="settings", default=None,)

from .device_management_configuration_setting import DeviceManagementConfigurationSetting

