from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsWindows10DevicesSummary(BaseModel):
	unsupportedOSversionDeviceCount: Optional[int] = Field(default=None,alias="unsupportedOSversionDeviceCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


