from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserLastSignInRecommendationInsightSetting(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	recommendationLookBackDuration: Optional[str] = Field(default=None,alias="recommendationLookBackDuration",)
	signInScope: Optional[UserSignInRecommendationScope] = Field(default=None,alias="signInScope",)

from .user_sign_in_recommendation_scope import UserSignInRecommendationScope

