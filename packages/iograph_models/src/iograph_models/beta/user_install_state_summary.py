from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserInstallStateSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userInstallStateSummary"] = Field(alias="@odata.type", default="#microsoft.graph.userInstallStateSummary")
	failedDeviceCount: Optional[int] = Field(alias="failedDeviceCount", default=None,)
	installedDeviceCount: Optional[int] = Field(alias="installedDeviceCount", default=None,)
	notInstalledDeviceCount: Optional[int] = Field(alias="notInstalledDeviceCount", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)
	deviceStates: Optional[list[DeviceInstallState]] = Field(alias="deviceStates", default=None,)

from .device_install_state import DeviceInstallState
