from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceLocalCredentialInfo(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	credentials: Optional[list[DeviceLocalCredential]] = Field(default=None,alias="credentials",)
	deviceName: Optional[str] = Field(default=None,alias="deviceName",)
	lastBackupDateTime: Optional[datetime] = Field(default=None,alias="lastBackupDateTime",)
	refreshDateTime: Optional[datetime] = Field(default=None,alias="refreshDateTime",)

from .device_local_credential import DeviceLocalCredential

