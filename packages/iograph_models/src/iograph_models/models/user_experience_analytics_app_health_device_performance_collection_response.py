from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAppHealthDevicePerformanceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[UserExperienceAnalyticsAppHealthDevicePerformance] = Field(alias="value",)

from .user_experience_analytics_app_health_device_performance import UserExperienceAnalyticsAppHealthDevicePerformance

