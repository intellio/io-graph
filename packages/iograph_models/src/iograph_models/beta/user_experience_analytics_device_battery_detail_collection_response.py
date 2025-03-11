from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsDeviceBatteryDetailCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[UserExperienceAnalyticsDeviceBatteryDetail]] = Field(alias="value",default=None,)

from .user_experience_analytics_device_battery_detail import UserExperienceAnalyticsDeviceBatteryDetail

