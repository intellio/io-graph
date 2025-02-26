from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessReviewStageSettings(BaseModel):
	decisionsThatWillMoveToNextStage: list[Optional[str]] = Field(alias="decisionsThatWillMoveToNextStage",)
	dependsOn: list[str] = Field(alias="dependsOn",)
	durationInDays: Optional[int] = Field(default=None,alias="durationInDays",)
	fallbackReviewers: list[AccessReviewReviewerScope] = Field(alias="fallbackReviewers",)
	recommendationInsightSettings: list[AccessReviewRecommendationInsightSetting] = Field(alias="recommendationInsightSettings",)
	recommendationsEnabled: Optional[bool] = Field(default=None,alias="recommendationsEnabled",)
	reviewers: list[AccessReviewReviewerScope] = Field(alias="reviewers",)
	stageId: Optional[str] = Field(default=None,alias="stageId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .access_review_reviewer_scope import AccessReviewReviewerScope
from .access_review_recommendation_insight_setting import AccessReviewRecommendationInsightSetting
from .access_review_reviewer_scope import AccessReviewReviewerScope

