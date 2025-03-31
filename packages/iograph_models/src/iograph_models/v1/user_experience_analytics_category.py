from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsCategory(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsCategory"] = Field(alias="@odata.type",)
	insights: Optional[list[UserExperienceAnalyticsInsight]] = Field(alias="insights", default=None,)
	metricValues: Optional[list[UserExperienceAnalyticsMetric]] = Field(alias="metricValues", default=None,)

from .user_experience_analytics_insight import UserExperienceAnalyticsInsight
from .user_experience_analytics_metric import UserExperienceAnalyticsMetric
