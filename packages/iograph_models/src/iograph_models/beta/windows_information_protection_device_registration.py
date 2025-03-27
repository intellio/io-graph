from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsInformationProtectionDeviceRegistration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	deviceMacAddress: Optional[str] = Field(alias="deviceMacAddress", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	deviceRegistrationId: Optional[str] = Field(alias="deviceRegistrationId", default=None,)
	deviceType: Optional[str] = Field(alias="deviceType", default=None,)
	lastCheckInDateTime: Optional[datetime] = Field(alias="lastCheckInDateTime", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)


