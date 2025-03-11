from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceLocalCredentialInfo(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	credentials: Optional[list[DeviceLocalCredential]] = Field(alias="credentials",default=None,)
	deviceName: Optional[str] = Field(alias="deviceName",default=None,)
	lastBackupDateTime: Optional[datetime] = Field(alias="lastBackupDateTime",default=None,)
	refreshDateTime: Optional[datetime] = Field(alias="refreshDateTime",default=None,)

from .device_local_credential import DeviceLocalCredential

