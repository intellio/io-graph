from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsCategory(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	insights: Optional[list[UserExperienceAnalyticsInsight]] = Field(default=None,alias="insights",)
	metricValues: Optional[list[UserExperienceAnalyticsMetric]] = Field(default=None,alias="metricValues",)

from .user_experience_analytics_insight import UserExperienceAnalyticsInsight
from .user_experience_analytics_metric import UserExperienceAnalyticsMetric

