from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class AccessReviewStageSettings(BaseModel):
	decisionsThatWillMoveToNextStage: Optional[list[str]] = Field(alias="decisionsThatWillMoveToNextStage", default=None,)
	dependsOn: Optional[list[str]] = Field(alias="dependsOn", default=None,)
	durationInDays: Optional[int] = Field(alias="durationInDays", default=None,)
	fallbackReviewers: Optional[list[AccessReviewReviewerScope]] = Field(alias="fallbackReviewers", default=None,)
	recommendationInsightSettings: Optional[list[Annotated[Union[GroupPeerOutlierRecommendationInsightSettings, UserLastSignInRecommendationInsightSetting],Field(discriminator="odata_type")]]] = Field(alias="recommendationInsightSettings", default=None,)
	recommendationsEnabled: Optional[bool] = Field(alias="recommendationsEnabled", default=None,)
	reviewers: Optional[list[AccessReviewReviewerScope]] = Field(alias="reviewers", default=None,)
	stageId: Optional[str] = Field(alias="stageId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .access_review_reviewer_scope import AccessReviewReviewerScope
from .group_peer_outlier_recommendation_insight_settings import GroupPeerOutlierRecommendationInsightSettings
from .user_last_sign_in_recommendation_insight_setting import UserLastSignInRecommendationInsightSetting
