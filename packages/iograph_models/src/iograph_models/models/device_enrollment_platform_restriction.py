from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceEnrollmentPlatformRestriction(BaseModel):
	osMaximumVersion: Optional[str] = Field(default=None,alias="osMaximumVersion",)
	osMinimumVersion: Optional[str] = Field(default=None,alias="osMinimumVersion",)
	personalDeviceEnrollmentBlocked: Optional[bool] = Field(default=None,alias="personalDeviceEnrollmentBlocked",)
	platformBlocked: Optional[bool] = Field(default=None,alias="platformBlocked",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


