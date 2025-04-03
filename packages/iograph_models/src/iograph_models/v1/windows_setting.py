from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WindowsSetting(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsSetting"] = Field(alias="@odata.type", default="#microsoft.graph.windowsSetting")
	payloadType: Optional[str] = Field(alias="payloadType", default=None,)
	settingType: Optional[WindowsSettingType | str] = Field(alias="settingType", default=None,)
	windowsDeviceId: Optional[str] = Field(alias="windowsDeviceId", default=None,)
	instances: Optional[list[WindowsSettingInstance]] = Field(alias="instances", default=None,)

from .windows_setting_type import WindowsSettingType
from .windows_setting_instance import WindowsSettingInstance
