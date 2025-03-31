from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsOverview(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsOverview"] = Field(alias="@odata.type",)
	insights: Optional[list[UserExperienceAnalyticsInsight]] = Field(alias="insights", default=None,)

from .user_experience_analytics_insight import UserExperienceAnalyticsInsight
