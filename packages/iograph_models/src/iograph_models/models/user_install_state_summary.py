from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserInstallStateSummary(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	failedDeviceCount: Optional[int] = Field(default=None,alias="failedDeviceCount",)
	installedDeviceCount: Optional[int] = Field(default=None,alias="installedDeviceCount",)
	notInstalledDeviceCount: Optional[int] = Field(default=None,alias="notInstalledDeviceCount",)
	userName: Optional[str] = Field(default=None,alias="userName",)
	deviceStates: list[DeviceInstallState] = Field(alias="deviceStates",)

from .device_install_state import DeviceInstallState

