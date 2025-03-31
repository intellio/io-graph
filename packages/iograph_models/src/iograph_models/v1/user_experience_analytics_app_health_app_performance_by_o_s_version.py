from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsAppHealthAppPerformanceByOSVersion"] = Field(alias="@odata.type",)
	activeDeviceCount: Optional[int] = Field(alias="activeDeviceCount", default=None,)
	appCrashCount: Optional[int] = Field(alias="appCrashCount", default=None,)
	appDisplayName: Optional[str] = Field(alias="appDisplayName", default=None,)
	appName: Optional[str] = Field(alias="appName", default=None,)
	appPublisher: Optional[str] = Field(alias="appPublisher", default=None,)
	appUsageDuration: Optional[int] = Field(alias="appUsageDuration", default=None,)
	meanTimeToFailureInMinutes: Optional[int] = Field(alias="meanTimeToFailureInMinutes", default=None,)
	osBuildNumber: Optional[str] = Field(alias="osBuildNumber", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)

