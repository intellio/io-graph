from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceEnrollmentPlatformRestriction(BaseModel):
	blockedManufacturers: Optional[list[str]] = Field(alias="blockedManufacturers", default=None,)
	blockedSkus: Optional[list[str]] = Field(alias="blockedSkus", default=None,)
	osMaximumVersion: Optional[str] = Field(alias="osMaximumVersion", default=None,)
	osMinimumVersion: Optional[str] = Field(alias="osMinimumVersion", default=None,)
	personalDeviceEnrollmentBlocked: Optional[bool] = Field(alias="personalDeviceEnrollmentBlocked", default=None,)
	platformBlocked: Optional[bool] = Field(alias="platformBlocked", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

