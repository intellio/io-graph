from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceEnrollmentWindowsHelloForBusinessConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[DeviceEnrollmentWindowsHelloForBusinessConfiguration]] = Field(default=None,alias="value",)

from .device_enrollment_windows_hello_for_business_configuration import DeviceEnrollmentWindowsHelloForBusinessConfiguration

