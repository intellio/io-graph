from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsModelScores(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsModelScores"] = Field(alias="@odata.type", default="#microsoft.graph.userExperienceAnalyticsModelScores")
	appReliabilityScore: float | str | ReferenceNumeric
	batteryHealthScore: float | str | ReferenceNumeric
	endpointAnalyticsScore: float | str | ReferenceNumeric
	healthStatus: Optional[UserExperienceAnalyticsHealthState | str] = Field(alias="healthStatus", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	modelDeviceCount: Optional[int] = Field(alias="modelDeviceCount", default=None,)
	startupPerformanceScore: float | str | ReferenceNumeric
	workFromAnywhereScore: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
