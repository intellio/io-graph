from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAppHealthDeviceModelPerformance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsAppHealthDeviceModelPerformance"] = Field(alias="@odata.type",)
	activeDeviceCount: Optional[int] = Field(alias="activeDeviceCount", default=None,)
	deviceManufacturer: Optional[str] = Field(alias="deviceManufacturer", default=None,)
	deviceModel: Optional[str] = Field(alias="deviceModel", default=None,)
	healthStatus: Optional[UserExperienceAnalyticsHealthState | str] = Field(alias="healthStatus", default=None,)
	meanTimeToFailureInMinutes: Optional[int] = Field(alias="meanTimeToFailureInMinutes", default=None,)
	modelAppHealthScore: float | str | ReferenceNumeric

from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
from .reference_numeric import ReferenceNumeric
