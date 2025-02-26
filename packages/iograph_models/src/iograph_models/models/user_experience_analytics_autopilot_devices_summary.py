from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAutopilotDevicesSummary(BaseModel):
	devicesNotAutopilotRegistered: Optional[int] = Field(default=None,alias="devicesNotAutopilotRegistered",)
	devicesWithoutAutopilotProfileAssigned: Optional[int] = Field(default=None,alias="devicesWithoutAutopilotProfileAssigned",)
	totalWindows10DevicesWithoutTenantAttached: Optional[int] = Field(default=None,alias="totalWindows10DevicesWithoutTenantAttached",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


