from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsAppHealthDeviceModelPerformance(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activeDeviceCount: Optional[int] = Field(default=None,alias="activeDeviceCount",)
	deviceManufacturer: Optional[str] = Field(default=None,alias="deviceManufacturer",)
	deviceModel: Optional[str] = Field(default=None,alias="deviceModel",)
	healthStatus: Optional[UserExperienceAnalyticsHealthState] = Field(default=None,alias="healthStatus",)
	meanTimeToFailureInMinutes: Optional[int] = Field(default=None,alias="meanTimeToFailureInMinutes",)
	modelAppHealthScore: float | str | ReferenceNumeric

from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
from .reference_numeric import ReferenceNumeric

