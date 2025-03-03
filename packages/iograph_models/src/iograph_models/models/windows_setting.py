from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsSetting(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	payloadType: Optional[str] = Field(default=None,alias="payloadType",)
	settingType: Optional[WindowsSettingType] = Field(default=None,alias="settingType",)
	windowsDeviceId: Optional[str] = Field(default=None,alias="windowsDeviceId",)
	instances: Optional[list[WindowsSettingInstance]] = Field(default=None,alias="instances",)

from .windows_setting_type import WindowsSettingType
from .windows_setting_instance import WindowsSettingInstance

