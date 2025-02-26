from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsWorkFromAnywhereDeviceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[UserExperienceAnalyticsWorkFromAnywhereDevice] = Field(alias="value",)

from .user_experience_analytics_work_from_anywhere_device import UserExperienceAnalyticsWorkFromAnywhereDevice

