from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceEnrollmentLimitConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[DeviceEnrollmentLimitConfiguration]] = Field(default=None,alias="value",)

from .device_enrollment_limit_configuration import DeviceEnrollmentLimitConfiguration

