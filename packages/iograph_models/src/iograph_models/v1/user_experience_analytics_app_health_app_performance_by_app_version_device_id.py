from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId"] = Field(alias="@odata.type", default="#microsoft.graph.userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId")
	appCrashCount: Optional[int] = Field(alias="appCrashCount", default=None,)
	appDisplayName: Optional[str] = Field(alias="appDisplayName", default=None,)
	appName: Optional[str] = Field(alias="appName", default=None,)
	appPublisher: Optional[str] = Field(alias="appPublisher", default=None,)
	appVersion: Optional[str] = Field(alias="appVersion", default=None,)
	deviceDisplayName: Optional[str] = Field(alias="deviceDisplayName", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	processedDateTime: Optional[datetime] = Field(alias="processedDateTime", default=None,)

