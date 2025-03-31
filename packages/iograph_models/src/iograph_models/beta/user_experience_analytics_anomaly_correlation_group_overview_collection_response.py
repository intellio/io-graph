from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAnomalyCorrelationGroupOverviewCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[UserExperienceAnalyticsAnomalyCorrelationGroupOverview]] = Field(alias="value", default=None,)

from .user_experience_analytics_anomaly_correlation_group_overview import UserExperienceAnalyticsAnomalyCorrelationGroupOverview
