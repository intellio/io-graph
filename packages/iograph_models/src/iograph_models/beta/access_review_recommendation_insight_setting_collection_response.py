from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewRecommendationInsightSettingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[GroupPeerOutlierRecommendationInsightSettings, UserLastSignInRecommendationInsightSetting]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .group_peer_outlier_recommendation_insight_settings import GroupPeerOutlierRecommendationInsightSettings
from .user_last_sign_in_recommendation_insight_setting import UserLastSignInRecommendationInsightSetting

