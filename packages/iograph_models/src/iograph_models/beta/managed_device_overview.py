from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedDeviceOverview(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedDeviceOverview"] = Field(alias="@odata.type",)
	deviceExchangeAccessStateSummary: Optional[DeviceExchangeAccessStateSummary] = Field(alias="deviceExchangeAccessStateSummary", default=None,)
	deviceOperatingSystemSummary: Optional[DeviceOperatingSystemSummary] = Field(alias="deviceOperatingSystemSummary", default=None,)
	dualEnrolledDeviceCount: Optional[int] = Field(alias="dualEnrolledDeviceCount", default=None,)
	enrolledDeviceCount: Optional[int] = Field(alias="enrolledDeviceCount", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	managedDeviceModelsAndManufacturers: Optional[ManagedDeviceModelsAndManufacturers] = Field(alias="managedDeviceModelsAndManufacturers", default=None,)
	mdmEnrolledCount: Optional[int] = Field(alias="mdmEnrolledCount", default=None,)

from .device_exchange_access_state_summary import DeviceExchangeAccessStateSummary
from .device_operating_system_summary import DeviceOperatingSystemSummary
from .managed_device_models_and_manufacturers import ManagedDeviceModelsAndManufacturers
