from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsWorkFromAnywhereModelPerformance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereModelPerformance"] = Field(alias="@odata.type", default="#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereModelPerformance")
	cloudIdentityScore: float | str | ReferenceNumeric
	cloudManagementScore: float | str | ReferenceNumeric
	cloudProvisioningScore: float | str | ReferenceNumeric
	healthStatus: Optional[UserExperienceAnalyticsHealthState | str] = Field(alias="healthStatus", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	modelDeviceCount: Optional[int] = Field(alias="modelDeviceCount", default=None,)
	windowsScore: float | str | ReferenceNumeric
	workFromAnywhereScore: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
