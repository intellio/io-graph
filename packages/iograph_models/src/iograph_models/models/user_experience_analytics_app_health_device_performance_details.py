from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsAppHealthDevicePerformanceDetails(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appDisplayName: Optional[str] = Field(default=None,alias="appDisplayName",)
	appPublisher: Optional[str] = Field(default=None,alias="appPublisher",)
	appVersion: Optional[str] = Field(default=None,alias="appVersion",)
	deviceDisplayName: Optional[str] = Field(default=None,alias="deviceDisplayName",)
	deviceId: Optional[str] = Field(default=None,alias="deviceId",)
	eventDateTime: Optional[datetime] = Field(default=None,alias="eventDateTime",)
	eventType: Optional[str] = Field(default=None,alias="eventType",)


