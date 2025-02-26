from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAppHealthOSVersionPerformanceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[UserExperienceAnalyticsAppHealthOSVersionPerformance] = Field(alias="value",)

from .user_experience_analytics_app_health_o_s_version_performance import UserExperienceAnalyticsAppHealthOSVersionPerformance

