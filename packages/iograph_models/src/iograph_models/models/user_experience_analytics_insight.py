from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsInsight(BaseModel):
	insightId: Optional[str] = Field(default=None,alias="insightId",)
	severity: Optional[UserExperienceAnalyticsInsightSeverity] = Field(default=None,alias="severity",)
	userExperienceAnalyticsMetricId: Optional[str] = Field(default=None,alias="userExperienceAnalyticsMetricId",)
	values: list[UserExperienceAnalyticsInsightValue] = Field(alias="values",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .user_experience_analytics_insight_severity import UserExperienceAnalyticsInsightSeverity
from .user_experience_analytics_insight_value import UserExperienceAnalyticsInsightValue

