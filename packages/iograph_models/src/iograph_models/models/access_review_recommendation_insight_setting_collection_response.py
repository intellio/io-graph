from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessReviewRecommendationInsightSettingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[AccessReviewRecommendationInsightSetting]] = Field(default=None,alias="value",)

from .access_review_recommendation_insight_setting import AccessReviewRecommendationInsightSetting

