from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewScheduleSettings(BaseModel):
	applyActions: SerializeAsAny[Optional[list[AccessReviewApplyAction]]] = Field(alias="applyActions",default=None,)
	autoApplyDecisionsEnabled: Optional[bool] = Field(alias="autoApplyDecisionsEnabled",default=None,)
	decisionHistoriesForReviewersEnabled: Optional[bool] = Field(alias="decisionHistoriesForReviewersEnabled",default=None,)
	defaultDecision: Optional[str] = Field(alias="defaultDecision",default=None,)
	defaultDecisionEnabled: Optional[bool] = Field(alias="defaultDecisionEnabled",default=None,)
	instanceDurationInDays: Optional[int] = Field(alias="instanceDurationInDays",default=None,)
	justificationRequiredOnApproval: Optional[bool] = Field(alias="justificationRequiredOnApproval",default=None,)
	mailNotificationsEnabled: Optional[bool] = Field(alias="mailNotificationsEnabled",default=None,)
	recommendationInsightSettings: SerializeAsAny[Optional[list[AccessReviewRecommendationInsightSetting]]] = Field(alias="recommendationInsightSettings",default=None,)
	recommendationLookBackDuration: Optional[str] = Field(alias="recommendationLookBackDuration",default=None,)
	recommendationsEnabled: Optional[bool] = Field(alias="recommendationsEnabled",default=None,)
	recurrence: Optional[PatternedRecurrence] = Field(alias="recurrence",default=None,)
	reminderNotificationsEnabled: Optional[bool] = Field(alias="reminderNotificationsEnabled",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .access_review_apply_action import AccessReviewApplyAction
from .access_review_recommendation_insight_setting import AccessReviewRecommendationInsightSetting
from .patterned_recurrence import PatternedRecurrence

