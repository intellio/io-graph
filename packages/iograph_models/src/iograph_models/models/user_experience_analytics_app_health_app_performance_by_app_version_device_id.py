from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appCrashCount: Optional[int] = Field(default=None,alias="appCrashCount",)
	appDisplayName: Optional[str] = Field(default=None,alias="appDisplayName",)
	appName: Optional[str] = Field(default=None,alias="appName",)
	appPublisher: Optional[str] = Field(default=None,alias="appPublisher",)
	appVersion: Optional[str] = Field(default=None,alias="appVersion",)
	deviceDisplayName: Optional[str] = Field(default=None,alias="deviceDisplayName",)
	deviceId: Optional[str] = Field(default=None,alias="deviceId",)
	processedDateTime: Optional[datetime] = Field(default=None,alias="processedDateTime",)


