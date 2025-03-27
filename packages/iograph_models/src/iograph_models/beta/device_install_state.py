from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceInstallState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	errorCode: Optional[str] = Field(alias="errorCode", default=None,)
	installState: Optional[InstallState | str] = Field(alias="installState", default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime", default=None,)
	osDescription: Optional[str] = Field(alias="osDescription", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)

from .install_state import InstallState

