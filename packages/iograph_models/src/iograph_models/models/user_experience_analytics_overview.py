from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsOverview(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	insights: Optional[list[UserExperienceAnalyticsInsight]] = Field(default=None,alias="insights",)

from .user_experience_analytics_insight import UserExperienceAnalyticsInsight

