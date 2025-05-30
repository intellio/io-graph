from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsWindows10DevicesSummary(BaseModel):
	unsupportedOSversionDeviceCount: Optional[int] = Field(alias="unsupportedOSversionDeviceCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

