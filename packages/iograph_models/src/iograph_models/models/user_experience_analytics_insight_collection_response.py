from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsInsightCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[UserExperienceAnalyticsInsight] = Field(alias="value",)

from .user_experience_analytics_insight import UserExperienceAnalyticsInsight

