from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsWorkFromAnywhereMetricCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[UserExperienceAnalyticsWorkFromAnywhereMetric]] = Field(alias="value", default=None,)

from .user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric

