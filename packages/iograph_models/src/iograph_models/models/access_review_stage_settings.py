from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessReviewStageSettings(BaseModel):
	decisionsThatWillMoveToNextStage: Optional[list[str]] = Field(default=None,alias="decisionsThatWillMoveToNextStage",)
	dependsOn: Optional[list[str]] = Field(default=None,alias="dependsOn",)
	durationInDays: Optional[int] = Field(default=None,alias="durationInDays",)
	fallbackReviewers: Optional[list[AccessReviewReviewerScope]] = Field(default=None,alias="fallbackReviewers",)
	recommendationInsightSettings: Optional[list[AccessReviewRecommendationInsightSetting]] = Field(default=None,alias="recommendationInsightSettings",)
	recommendationsEnabled: Optional[bool] = Field(default=None,alias="recommendationsEnabled",)
	reviewers: Optional[list[AccessReviewReviewerScope]] = Field(default=None,alias="reviewers",)
	stageId: Optional[str] = Field(default=None,alias="stageId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .access_review_reviewer_scope import AccessReviewReviewerScope
from .access_review_recommendation_insight_setting import AccessReviewRecommendationInsightSetting
from .access_review_reviewer_scope import AccessReviewReviewerScope

