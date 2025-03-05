from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserLastSignInRecommendationInsightSetting(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	recommendationLookBackDuration: Optional[str] = Field(alias="recommendationLookBackDuration",default=None,)
	signInScope: Optional[UserSignInRecommendationScope | str] = Field(alias="signInScope",default=None,)

from .user_sign_in_recommendation_scope import UserSignInRecommendationScope

