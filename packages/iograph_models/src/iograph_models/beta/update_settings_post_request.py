from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Update_settingsPostRequest(BaseModel):
	settings: SerializeAsAny[Optional[list[DeviceManagementSettingInstance]]] = Field(alias="settings",default=None,)

from .device_management_setting_instance import DeviceManagementSettingInstance

