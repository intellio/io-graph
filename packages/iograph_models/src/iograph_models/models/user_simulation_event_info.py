from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserSimulationEventInfo(BaseModel):
	browser: Optional[str] = Field(default=None,alias="browser",)
	clickSource: Optional[ClickSource] = Field(default=None,alias="clickSource",)
	eventDateTime: Optional[datetime] = Field(default=None,alias="eventDateTime",)
	eventName: Optional[str] = Field(default=None,alias="eventName",)
	ipAddress: Optional[str] = Field(default=None,alias="ipAddress",)
	osPlatformDeviceDetails: Optional[str] = Field(default=None,alias="osPlatformDeviceDetails",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .click_source import ClickSource

