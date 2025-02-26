from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAppHealthAppPerformanceByOSVersionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion] = Field(alias="value",)

from .user_experience_analytics_app_health_app_performance_by_o_s_version import UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion

