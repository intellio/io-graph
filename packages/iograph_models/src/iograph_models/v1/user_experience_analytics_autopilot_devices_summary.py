from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsAutopilotDevicesSummary(BaseModel):
	devicesNotAutopilotRegistered: Optional[int] = Field(alias="devicesNotAutopilotRegistered", default=None,)
	devicesWithoutAutopilotProfileAssigned: Optional[int] = Field(alias="devicesWithoutAutopilotProfileAssigned", default=None,)
	totalWindows10DevicesWithoutTenantAttached: Optional[int] = Field(alias="totalWindows10DevicesWithoutTenantAttached", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


