from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAppHealthApplicationPerformance(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activeDeviceCount: Optional[int] = Field(default=None,alias="activeDeviceCount",)
	appCrashCount: Optional[int] = Field(default=None,alias="appCrashCount",)
	appDisplayName: Optional[str] = Field(default=None,alias="appDisplayName",)
	appHangCount: Optional[int] = Field(default=None,alias="appHangCount",)
	appHealthScore: Optional[float] | Optional[str] | ReferenceNumeric
	appName: Optional[str] = Field(default=None,alias="appName",)
	appPublisher: Optional[str] = Field(default=None,alias="appPublisher",)
	appUsageDuration: Optional[int] = Field(default=None,alias="appUsageDuration",)
	meanTimeToFailureInMinutes: Optional[int] = Field(default=None,alias="meanTimeToFailureInMinutes",)

from .reference_numeric import ReferenceNumeric

