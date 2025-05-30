from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceInstallState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceInstallState"] = Field(alias="@odata.type", default="#microsoft.graph.deviceInstallState")
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	errorCode: Optional[str] = Field(alias="errorCode", default=None,)
	installState: Optional[InstallState | str] = Field(alias="installState", default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime", default=None,)
	osDescription: Optional[str] = Field(alias="osDescription", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)

from .install_state import InstallState
