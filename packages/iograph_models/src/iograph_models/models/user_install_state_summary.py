from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserInstallStateSummary(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	failedDeviceCount: Optional[int] = Field(alias="failedDeviceCount",default=None,)
	installedDeviceCount: Optional[int] = Field(alias="installedDeviceCount",default=None,)
	notInstalledDeviceCount: Optional[int] = Field(alias="notInstalledDeviceCount",default=None,)
	userName: Optional[str] = Field(alias="userName",default=None,)
	deviceStates: Optional[list[DeviceInstallState]] = Field(alias="deviceStates",default=None,)

from .device_install_state import DeviceInstallState

