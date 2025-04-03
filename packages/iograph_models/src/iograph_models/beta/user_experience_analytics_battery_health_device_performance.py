from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsBatteryHealthDevicePerformance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsBatteryHealthDevicePerformance"] = Field(alias="@odata.type", default="#microsoft.graph.userExperienceAnalyticsBatteryHealthDevicePerformance")
	batteryAgeInDays: Optional[int] = Field(alias="batteryAgeInDays", default=None,)
	deviceBatteriesDetails: Optional[list[UserExperienceAnalyticsDeviceBatteryDetail]] = Field(alias="deviceBatteriesDetails", default=None,)
	deviceBatteryCount: Optional[int] = Field(alias="deviceBatteryCount", default=None,)
	deviceBatteryHealthScore: Optional[int] = Field(alias="deviceBatteryHealthScore", default=None,)
	deviceBatteryTags: Optional[list[str]] = Field(alias="deviceBatteryTags", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	deviceManufacturerName: Optional[str] = Field(alias="deviceManufacturerName", default=None,)
	deviceModelName: Optional[str] = Field(alias="deviceModelName", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	estimatedRuntimeInMinutes: Optional[int] = Field(alias="estimatedRuntimeInMinutes", default=None,)
	fullBatteryDrainCount: Optional[int] = Field(alias="fullBatteryDrainCount", default=None,)
	healthStatus: Optional[UserExperienceAnalyticsHealthState | str] = Field(alias="healthStatus", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	maxCapacityPercentage: Optional[int] = Field(alias="maxCapacityPercentage", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)

from .user_experience_analytics_device_battery_detail import UserExperienceAnalyticsDeviceBatteryDetail
from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
