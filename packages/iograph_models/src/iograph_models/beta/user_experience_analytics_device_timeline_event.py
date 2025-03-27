from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsDeviceTimelineEvent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime", default=None,)
	eventDetails: Optional[str] = Field(alias="eventDetails", default=None,)
	eventLevel: Optional[DeviceEventLevel | str] = Field(alias="eventLevel", default=None,)
	eventName: Optional[str] = Field(alias="eventName", default=None,)
	eventSource: Optional[str] = Field(alias="eventSource", default=None,)

from .device_event_level import DeviceEventLevel

