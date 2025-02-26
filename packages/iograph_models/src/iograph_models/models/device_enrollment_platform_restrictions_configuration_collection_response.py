from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceEnrollmentPlatformRestrictionsConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[DeviceEnrollmentPlatformRestrictionsConfiguration] = Field(alias="value",)

from .device_enrollment_platform_restrictions_configuration import DeviceEnrollmentPlatformRestrictionsConfiguration

