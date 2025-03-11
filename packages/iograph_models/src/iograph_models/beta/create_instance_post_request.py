from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Create_instancePostRequest(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	settingsDelta: SerializeAsAny[Optional[list[DeviceManagementSettingInstance]]] = Field(alias="settingsDelta",default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds",default=None,)

from .device_management_setting_instance import DeviceManagementSettingInstance

