from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewRecommendationInsightSettingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[AccessReviewRecommendationInsightSetting]]] = Field(alias="value",default=None,)

from .access_review_recommendation_insight_setting import AccessReviewRecommendationInsightSetting

