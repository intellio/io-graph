from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsBatteryHealthOsPerformance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	activeDevices: Optional[int] = Field(alias="activeDevices", default=None,)
	averageBatteryAgeInDays: Optional[int] = Field(alias="averageBatteryAgeInDays", default=None,)
	averageEstimatedRuntimeInMinutes: Optional[int] = Field(alias="averageEstimatedRuntimeInMinutes", default=None,)
	averageMaxCapacityPercentage: Optional[int] = Field(alias="averageMaxCapacityPercentage", default=None,)
	meanFullBatteryDrainCount: Optional[int] = Field(alias="meanFullBatteryDrainCount", default=None,)
	medianEstimatedRuntimeInMinutes: Optional[int] = Field(alias="medianEstimatedRuntimeInMinutes", default=None,)
	medianFullBatteryDrainCount: Optional[int] = Field(alias="medianFullBatteryDrainCount", default=None,)
	medianMaxCapacityPercentage: Optional[int] = Field(alias="medianMaxCapacityPercentage", default=None,)
	osBatteryHealthScore: Optional[int] = Field(alias="osBatteryHealthScore", default=None,)
	osBuildNumber: Optional[str] = Field(alias="osBuildNumber", default=None,)
	osHealthStatus: Optional[UserExperienceAnalyticsHealthState | str] = Field(alias="osHealthStatus", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)

from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

