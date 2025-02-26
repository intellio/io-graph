from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsWorkFromAnywhereMetric(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	metricDevices: list[UserExperienceAnalyticsWorkFromAnywhereDevice] = Field(alias="metricDevices",)

from .user_experience_analytics_work_from_anywhere_device import UserExperienceAnalyticsWorkFromAnywhereDevice

