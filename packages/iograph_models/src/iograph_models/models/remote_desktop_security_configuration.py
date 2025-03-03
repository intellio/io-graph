from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RemoteDesktopSecurityConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isRemoteDesktopProtocolEnabled: Optional[bool] = Field(default=None,alias="isRemoteDesktopProtocolEnabled",)
	targetDeviceGroups: Optional[list[TargetDeviceGroup]] = Field(default=None,alias="targetDeviceGroups",)

from .target_device_group import TargetDeviceGroup

