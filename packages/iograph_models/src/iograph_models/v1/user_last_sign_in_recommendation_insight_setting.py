from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserLastSignInRecommendationInsightSetting(BaseModel):
	odata_type: Literal["#microsoft.graph.userLastSignInRecommendationInsightSetting"] = Field(alias="@odata.type", default="#microsoft.graph.userLastSignInRecommendationInsightSetting")
	recommendationLookBackDuration: Optional[str] = Field(alias="recommendationLookBackDuration", default=None,)
	signInScope: Optional[UserSignInRecommendationScope | str] = Field(alias="signInScope", default=None,)

from .user_sign_in_recommendation_scope import UserSignInRecommendationScope
