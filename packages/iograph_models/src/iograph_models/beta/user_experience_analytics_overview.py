from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsOverview(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	insights: Optional[list[UserExperienceAnalyticsInsight]] = Field(alias="insights",default=None,)

from .user_experience_analytics_insight import UserExperienceAnalyticsInsight

