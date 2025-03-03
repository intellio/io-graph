from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAppHealthDeviceModelPerformanceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[UserExperienceAnalyticsAppHealthDeviceModelPerformance]] = Field(default=None,alias="value",)

from .user_experience_analytics_app_health_device_model_performance import UserExperienceAnalyticsAppHealthDeviceModelPerformance

