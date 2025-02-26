from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceExchangeAccessStateSummary(BaseModel):
	allowedDeviceCount: Optional[int] = Field(default=None,alias="allowedDeviceCount",)
	blockedDeviceCount: Optional[int] = Field(default=None,alias="blockedDeviceCount",)
	quarantinedDeviceCount: Optional[int] = Field(default=None,alias="quarantinedDeviceCount",)
	unavailableDeviceCount: Optional[int] = Field(default=None,alias="unavailableDeviceCount",)
	unknownDeviceCount: Optional[int] = Field(default=None,alias="unknownDeviceCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


