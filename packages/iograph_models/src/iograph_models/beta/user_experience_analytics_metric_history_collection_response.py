from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsMetricHistoryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[UserExperienceAnalyticsMetricHistory]] = Field(alias="value", default=None,)

from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory
