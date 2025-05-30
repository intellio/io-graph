from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Summarize_device_resource_performance_with_summarizebyGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[UserExperienceAnalyticsResourcePerformance]] = Field(alias="value", default=None,)

from .user_experience_analytics_resource_performance import UserExperienceAnalyticsResourcePerformance
