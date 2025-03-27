from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Summarize_device_performance_devices_with_summarizebyGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[UserExperienceAnalyticsDevicePerformance]] = Field(alias="value", default=None,)

from .user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformance

