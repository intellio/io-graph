from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceComplianceDeviceStatusCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[DeviceComplianceDeviceStatus] = Field(alias="value",)

from .device_compliance_device_status import DeviceComplianceDeviceStatus

