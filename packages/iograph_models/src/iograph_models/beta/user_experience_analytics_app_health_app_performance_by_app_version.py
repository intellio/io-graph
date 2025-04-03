from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsAppHealthAppPerformanceByAppVersion"] = Field(alias="@odata.type", default="#microsoft.graph.userExperienceAnalyticsAppHealthAppPerformanceByAppVersion")
	appCrashCount: Optional[int] = Field(alias="appCrashCount", default=None,)
	appDisplayName: Optional[str] = Field(alias="appDisplayName", default=None,)
	appName: Optional[str] = Field(alias="appName", default=None,)
	appPublisher: Optional[str] = Field(alias="appPublisher", default=None,)
	appUsageDuration: Optional[int] = Field(alias="appUsageDuration", default=None,)
	appVersion: Optional[str] = Field(alias="appVersion", default=None,)
	meanTimeToFailureInMinutes: Optional[int] = Field(alias="meanTimeToFailureInMinutes", default=None,)

