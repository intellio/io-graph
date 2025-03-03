from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessReviewScheduleSettings(BaseModel):
	applyActions: Optional[list[AccessReviewApplyAction]] = Field(default=None,alias="applyActions",)
	autoApplyDecisionsEnabled: Optional[bool] = Field(default=None,alias="autoApplyDecisionsEnabled",)
	decisionHistoriesForReviewersEnabled: Optional[bool] = Field(default=None,alias="decisionHistoriesForReviewersEnabled",)
	defaultDecision: Optional[str] = Field(default=None,alias="defaultDecision",)
	defaultDecisionEnabled: Optional[bool] = Field(default=None,alias="defaultDecisionEnabled",)
	instanceDurationInDays: Optional[int] = Field(default=None,alias="instanceDurationInDays",)
	justificationRequiredOnApproval: Optional[bool] = Field(default=None,alias="justificationRequiredOnApproval",)
	mailNotificationsEnabled: Optional[bool] = Field(default=None,alias="mailNotificationsEnabled",)
	recommendationInsightSettings: Optional[list[AccessReviewRecommendationInsightSetting]] = Field(default=None,alias="recommendationInsightSettings",)
	recommendationLookBackDuration: Optional[str] = Field(default=None,alias="recommendationLookBackDuration",)
	recommendationsEnabled: Optional[bool] = Field(default=None,alias="recommendationsEnabled",)
	recurrence: Optional[PatternedRecurrence] = Field(default=None,alias="recurrence",)
	reminderNotificationsEnabled: Optional[bool] = Field(default=None,alias="reminderNotificationsEnabled",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .access_review_apply_action import AccessReviewApplyAction
from .access_review_recommendation_insight_setting import AccessReviewRecommendationInsightSetting
from .patterned_recurrence import PatternedRecurrence

