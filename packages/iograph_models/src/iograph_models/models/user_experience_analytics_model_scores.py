from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsModelScores(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appReliabilityScore: float | str | ReferenceNumeric
	batteryHealthScore: float | str | ReferenceNumeric
	endpointAnalyticsScore: float | str | ReferenceNumeric
	healthStatus: Optional[UserExperienceAnalyticsHealthState] = Field(default=None,alias="healthStatus",)
	manufacturer: Optional[str] = Field(default=None,alias="manufacturer",)
	model: Optional[str] = Field(default=None,alias="model",)
	modelDeviceCount: Optional[int] = Field(default=None,alias="modelDeviceCount",)
	startupPerformanceScore: float | str | ReferenceNumeric
	workFromAnywhereScore: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

