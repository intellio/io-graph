from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsWorkFromAnywhereMetric(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereMetric"] = Field(alias="@odata.type", default="#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereMetric")
	metricDevices: Optional[list[UserExperienceAnalyticsWorkFromAnywhereDevice]] = Field(alias="metricDevices", default=None,)

from .user_experience_analytics_work_from_anywhere_device import UserExperienceAnalyticsWorkFromAnywhereDevice
