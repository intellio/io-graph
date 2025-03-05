from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsInsight(BaseModel):
	insightId: Optional[str] = Field(alias="insightId",default=None,)
	severity: Optional[str | UserExperienceAnalyticsInsightSeverity] = Field(alias="severity",default=None,)
	userExperienceAnalyticsMetricId: Optional[str] = Field(alias="userExperienceAnalyticsMetricId",default=None,)
	values: SerializeAsAny[Optional[list[UserExperienceAnalyticsInsightValue]]] = Field(alias="values",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .user_experience_analytics_insight_severity import UserExperienceAnalyticsInsightSeverity
from .user_experience_analytics_insight_value import UserExperienceAnalyticsInsightValue

