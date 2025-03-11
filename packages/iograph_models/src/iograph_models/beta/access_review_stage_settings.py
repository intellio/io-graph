from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewStageSettings(BaseModel):
	decisionsThatWillMoveToNextStage: Optional[list[str]] = Field(alias="decisionsThatWillMoveToNextStage",default=None,)
	dependsOn: Optional[list[str]] = Field(alias="dependsOn",default=None,)
	durationInDays: Optional[int] = Field(alias="durationInDays",default=None,)
	fallbackReviewers: Optional[list[AccessReviewReviewerScope]] = Field(alias="fallbackReviewers",default=None,)
	recommendationInsightSettings: SerializeAsAny[Optional[list[AccessReviewRecommendationInsightSetting]]] = Field(alias="recommendationInsightSettings",default=None,)
	recommendationLookBackDuration: Optional[str] = Field(alias="recommendationLookBackDuration",default=None,)
	recommendationsEnabled: Optional[bool] = Field(alias="recommendationsEnabled",default=None,)
	reviewers: Optional[list[AccessReviewReviewerScope]] = Field(alias="reviewers",default=None,)
	stageId: Optional[str] = Field(alias="stageId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .access_review_reviewer_scope import AccessReviewReviewerScope
from .access_review_recommendation_insight_setting import AccessReviewRecommendationInsightSetting
from .access_review_reviewer_scope import AccessReviewReviewerScope

