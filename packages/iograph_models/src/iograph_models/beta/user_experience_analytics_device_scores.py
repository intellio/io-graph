from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsDeviceScores(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsDeviceScores"] = Field(alias="@odata.type",)
	appReliabilityScore: float | str | ReferenceNumeric
	batteryHealthScore: float | str | ReferenceNumeric
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	endpointAnalyticsScore: float | str | ReferenceNumeric
	healthStatus: Optional[UserExperienceAnalyticsHealthState | str] = Field(alias="healthStatus", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	meanResourceSpikeTimeScore: float | str | ReferenceNumeric
	model: Optional[str] = Field(alias="model", default=None,)
	startupPerformanceScore: float | str | ReferenceNumeric
	workFromAnywhereScore: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
