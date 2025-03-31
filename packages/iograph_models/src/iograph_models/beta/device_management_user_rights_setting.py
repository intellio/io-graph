from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceManagementUserRightsSetting(BaseModel):
	localUsersOrGroups: Optional[list[DeviceManagementUserRightsLocalUserOrGroup]] = Field(alias="localUsersOrGroups", default=None,)
	state: Optional[StateManagementSetting | str] = Field(alias="state", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_management_user_rights_local_user_or_group import DeviceManagementUserRightsLocalUserOrGroup
from .state_management_setting import StateManagementSetting
