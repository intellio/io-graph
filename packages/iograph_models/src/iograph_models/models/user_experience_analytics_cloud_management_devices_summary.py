from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsCloudManagementDevicesSummary(BaseModel):
	coManagedDeviceCount: Optional[int] = Field(default=None,alias="coManagedDeviceCount",)
	intuneDeviceCount: Optional[int] = Field(default=None,alias="intuneDeviceCount",)
	tenantAttachDeviceCount: Optional[int] = Field(default=None,alias="tenantAttachDeviceCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


