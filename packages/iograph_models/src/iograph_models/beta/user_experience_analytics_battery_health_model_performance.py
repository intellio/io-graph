from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsBatteryHealthModelPerformance(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	activeDevices: Optional[int] = Field(alias="activeDevices",default=None,)
	averageBatteryAgeInDays: Optional[int] = Field(alias="averageBatteryAgeInDays",default=None,)
	averageEstimatedRuntimeInMinutes: Optional[int] = Field(alias="averageEstimatedRuntimeInMinutes",default=None,)
	averageMaxCapacityPercentage: Optional[int] = Field(alias="averageMaxCapacityPercentage",default=None,)
	deviceManufacturerName: Optional[str] = Field(alias="deviceManufacturerName",default=None,)
	deviceModelName: Optional[str] = Field(alias="deviceModelName",default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer",default=None,)
	meanFullBatteryDrainCount: Optional[int] = Field(alias="meanFullBatteryDrainCount",default=None,)
	medianEstimatedRuntimeInMinutes: Optional[int] = Field(alias="medianEstimatedRuntimeInMinutes",default=None,)
	medianFullBatteryDrainCount: Optional[int] = Field(alias="medianFullBatteryDrainCount",default=None,)
	medianMaxCapacityPercentage: Optional[int] = Field(alias="medianMaxCapacityPercentage",default=None,)
	model: Optional[str] = Field(alias="model",default=None,)
	modelBatteryHealthScore: Optional[int] = Field(alias="modelBatteryHealthScore",default=None,)
	modelHealthStatus: Optional[UserExperienceAnalyticsHealthState | str] = Field(alias="modelHealthStatus",default=None,)

from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

