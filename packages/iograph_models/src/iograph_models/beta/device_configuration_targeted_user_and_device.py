from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceConfigurationTargetedUserAndDevice(BaseModel):
	deviceId: Optional[str] = Field(alias="deviceId",default=None,)
	deviceName: Optional[str] = Field(alias="deviceName",default=None,)
	lastCheckinDateTime: Optional[datetime] = Field(alias="lastCheckinDateTime",default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


