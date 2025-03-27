from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RemoteDesktopSecurityConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	isRemoteDesktopProtocolEnabled: Optional[bool] = Field(alias="isRemoteDesktopProtocolEnabled", default=None,)
	targetDeviceGroups: Optional[list[TargetDeviceGroup]] = Field(alias="targetDeviceGroups", default=None,)

from .target_device_group import TargetDeviceGroup

