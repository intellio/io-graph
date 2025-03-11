from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsManagementAppHealthState(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deviceName: Optional[str] = Field(alias="deviceName",default=None,)
	deviceOSVersion: Optional[str] = Field(alias="deviceOSVersion",default=None,)
	healthState: Optional[HealthState | str] = Field(alias="healthState",default=None,)
	installedVersion: Optional[str] = Field(alias="installedVersion",default=None,)
	lastCheckInDateTime: Optional[datetime] = Field(alias="lastCheckInDateTime",default=None,)

from .health_state import HealthState

