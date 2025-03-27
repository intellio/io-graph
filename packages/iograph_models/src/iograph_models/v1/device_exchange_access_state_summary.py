from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceExchangeAccessStateSummary(BaseModel):
	allowedDeviceCount: Optional[int] = Field(alias="allowedDeviceCount", default=None,)
	blockedDeviceCount: Optional[int] = Field(alias="blockedDeviceCount", default=None,)
	quarantinedDeviceCount: Optional[int] = Field(alias="quarantinedDeviceCount", default=None,)
	unavailableDeviceCount: Optional[int] = Field(alias="unavailableDeviceCount", default=None,)
	unknownDeviceCount: Optional[int] = Field(alias="unknownDeviceCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


