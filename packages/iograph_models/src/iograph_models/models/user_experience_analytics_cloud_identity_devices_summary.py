from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsCloudIdentityDevicesSummary(BaseModel):
	deviceWithoutCloudIdentityCount: Optional[int] = Field(default=None,alias="deviceWithoutCloudIdentityCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


