from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appCrashCount: Optional[int] = Field(alias="appCrashCount",default=None,)
	appDisplayName: Optional[str] = Field(alias="appDisplayName",default=None,)
	appName: Optional[str] = Field(alias="appName",default=None,)
	appPublisher: Optional[str] = Field(alias="appPublisher",default=None,)
	appVersion: Optional[str] = Field(alias="appVersion",default=None,)
	deviceCountWithCrashes: Optional[int] = Field(alias="deviceCountWithCrashes",default=None,)
	isLatestUsedVersion: Optional[bool] = Field(alias="isLatestUsedVersion",default=None,)
	isMostUsedVersion: Optional[bool] = Field(alias="isMostUsedVersion",default=None,)


