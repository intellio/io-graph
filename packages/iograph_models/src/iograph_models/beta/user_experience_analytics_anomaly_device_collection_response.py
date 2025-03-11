from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsAnomalyDeviceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[UserExperienceAnalyticsAnomalyDevice]] = Field(alias="value",default=None,)

from .user_experience_analytics_anomaly_device import UserExperienceAnalyticsAnomalyDevice

