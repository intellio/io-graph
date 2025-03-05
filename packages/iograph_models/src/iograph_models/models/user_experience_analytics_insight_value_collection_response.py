from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsInsightValueCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: SerializeAsAny[Optional[list[UserExperienceAnalyticsInsightValue]]] = Field(default=None,alias="value",)

from .user_experience_analytics_insight_value import UserExperienceAnalyticsInsightValue

