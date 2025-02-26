from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsModelScoresCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[UserExperienceAnalyticsModelScores] = Field(alias="value",)

from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores

