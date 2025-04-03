from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class RemoteDesktopSecurityConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.remoteDesktopSecurityConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.remoteDesktopSecurityConfiguration")
	isRemoteDesktopProtocolEnabled: Optional[bool] = Field(alias="isRemoteDesktopProtocolEnabled", default=None,)
	targetDeviceGroups: Optional[list[TargetDeviceGroup]] = Field(alias="targetDeviceGroups", default=None,)

from .target_device_group import TargetDeviceGroup
