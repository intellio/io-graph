from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsAppHealthDevicePerformanceDetails(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appDisplayName: Optional[str] = Field(alias="appDisplayName",default=None,)
	appPublisher: Optional[str] = Field(alias="appPublisher",default=None,)
	appVersion: Optional[str] = Field(alias="appVersion",default=None,)
	deviceDisplayName: Optional[str] = Field(alias="deviceDisplayName",default=None,)
	deviceId: Optional[str] = Field(alias="deviceId",default=None,)
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime",default=None,)
	eventType: Optional[str] = Field(alias="eventType",default=None,)


