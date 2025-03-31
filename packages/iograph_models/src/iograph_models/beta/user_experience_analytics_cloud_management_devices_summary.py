from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsCloudManagementDevicesSummary(BaseModel):
	coManagedDeviceCount: Optional[int] = Field(alias="coManagedDeviceCount", default=None,)
	intuneDeviceCount: Optional[int] = Field(alias="intuneDeviceCount", default=None,)
	tenantAttachDeviceCount: Optional[int] = Field(alias="tenantAttachDeviceCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

