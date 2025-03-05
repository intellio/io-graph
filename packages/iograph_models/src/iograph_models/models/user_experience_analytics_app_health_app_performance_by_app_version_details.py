from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appCrashCount: Optional[int] = Field(default=None,alias="appCrashCount",)
	appDisplayName: Optional[str] = Field(default=None,alias="appDisplayName",)
	appName: Optional[str] = Field(default=None,alias="appName",)
	appPublisher: Optional[str] = Field(default=None,alias="appPublisher",)
	appVersion: Optional[str] = Field(default=None,alias="appVersion",)
	deviceCountWithCrashes: Optional[int] = Field(default=None,alias="deviceCountWithCrashes",)
	isLatestUsedVersion: Optional[bool] = Field(default=None,alias="isLatestUsedVersion",)
	isMostUsedVersion: Optional[bool] = Field(default=None,alias="isMostUsedVersion",)


