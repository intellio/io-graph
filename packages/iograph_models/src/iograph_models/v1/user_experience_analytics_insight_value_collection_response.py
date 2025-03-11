from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsInsightValueCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[UserExperienceAnalyticsInsightValue]]] = Field(alias="value",default=None,)

from .user_experience_analytics_insight_value import UserExperienceAnalyticsInsightValue

