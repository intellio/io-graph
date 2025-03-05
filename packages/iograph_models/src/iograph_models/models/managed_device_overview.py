from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedDeviceOverview(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deviceExchangeAccessStateSummary: Optional[DeviceExchangeAccessStateSummary] = Field(default=None,alias="deviceExchangeAccessStateSummary",)
	deviceOperatingSystemSummary: Optional[DeviceOperatingSystemSummary] = Field(default=None,alias="deviceOperatingSystemSummary",)
	dualEnrolledDeviceCount: Optional[int] = Field(default=None,alias="dualEnrolledDeviceCount",)
	enrolledDeviceCount: Optional[int] = Field(default=None,alias="enrolledDeviceCount",)
	mdmEnrolledCount: Optional[int] = Field(default=None,alias="mdmEnrolledCount",)

from .device_exchange_access_state_summary import DeviceExchangeAccessStateSummary
from .device_operating_system_summary import DeviceOperatingSystemSummary

