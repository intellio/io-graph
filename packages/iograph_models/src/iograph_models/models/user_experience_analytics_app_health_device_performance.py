from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsAppHealthDevicePerformance(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appCrashCount: Optional[int] = Field(default=None,alias="appCrashCount",)
	appHangCount: Optional[int] = Field(default=None,alias="appHangCount",)
	crashedAppCount: Optional[int] = Field(default=None,alias="crashedAppCount",)
	deviceAppHealthScore: float | str | ReferenceNumeric
	deviceDisplayName: Optional[str] = Field(default=None,alias="deviceDisplayName",)
	deviceId: Optional[str] = Field(default=None,alias="deviceId",)
	deviceManufacturer: Optional[str] = Field(default=None,alias="deviceManufacturer",)
	deviceModel: Optional[str] = Field(default=None,alias="deviceModel",)
	healthStatus: Optional[UserExperienceAnalyticsHealthState] = Field(default=None,alias="healthStatus",)
	meanTimeToFailureInMinutes: Optional[int] = Field(default=None,alias="meanTimeToFailureInMinutes",)
	processedDateTime: Optional[datetime] = Field(default=None,alias="processedDateTime",)

from .reference_numeric import ReferenceNumeric
from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

