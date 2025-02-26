from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceInstallState(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deviceId: Optional[str] = Field(default=None,alias="deviceId",)
	deviceName: Optional[str] = Field(default=None,alias="deviceName",)
	errorCode: Optional[str] = Field(default=None,alias="errorCode",)
	installState: Optional[InstallState] = Field(default=None,alias="installState",)
	lastSyncDateTime: Optional[datetime] = Field(default=None,alias="lastSyncDateTime",)
	osDescription: Optional[str] = Field(default=None,alias="osDescription",)
	osVersion: Optional[str] = Field(default=None,alias="osVersion",)
	userName: Optional[str] = Field(default=None,alias="userName",)

from .install_state import InstallState

