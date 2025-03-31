from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class AccessReviewScheduleSettings(BaseModel):
	applyActions: Optional[list[Annotated[Union[DisableAndDeleteUserApplyAction, RemoveAccessApplyAction],Field(discriminator="odata_type")]]] = Field(alias="applyActions", default=None,)
	autoApplyDecisionsEnabled: Optional[bool] = Field(alias="autoApplyDecisionsEnabled", default=None,)
	decisionHistoriesForReviewersEnabled: Optional[bool] = Field(alias="decisionHistoriesForReviewersEnabled", default=None,)
	defaultDecision: Optional[str] = Field(alias="defaultDecision", default=None,)
	defaultDecisionEnabled: Optional[bool] = Field(alias="defaultDecisionEnabled", default=None,)
	instanceDurationInDays: Optional[int] = Field(alias="instanceDurationInDays", default=None,)
	justificationRequiredOnApproval: Optional[bool] = Field(alias="justificationRequiredOnApproval", default=None,)
	mailNotificationsEnabled: Optional[bool] = Field(alias="mailNotificationsEnabled", default=None,)
	recommendationInsightSettings: Optional[list[Annotated[Union[GroupPeerOutlierRecommendationInsightSettings, UserLastSignInRecommendationInsightSetting],Field(discriminator="odata_type")]]] = Field(alias="recommendationInsightSettings", default=None,)
	recommendationLookBackDuration: Optional[str] = Field(alias="recommendationLookBackDuration", default=None,)
	recommendationsEnabled: Optional[bool] = Field(alias="recommendationsEnabled", default=None,)
	recurrence: Optional[PatternedRecurrence] = Field(alias="recurrence", default=None,)
	reminderNotificationsEnabled: Optional[bool] = Field(alias="reminderNotificationsEnabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .disable_and_delete_user_apply_action import DisableAndDeleteUserApplyAction
from .remove_access_apply_action import RemoveAccessApplyAction
from .group_peer_outlier_recommendation_insight_settings import GroupPeerOutlierRecommendationInsightSettings
from .user_last_sign_in_recommendation_insight_setting import UserLastSignInRecommendationInsightSetting
from .patterned_recurrence import PatternedRecurrence
