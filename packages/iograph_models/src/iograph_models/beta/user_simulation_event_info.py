from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UserSimulationEventInfo(BaseModel):
	browser: Optional[str] = Field(alias="browser", default=None,)
	clickSource: Optional[ClickSource | str] = Field(alias="clickSource", default=None,)
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime", default=None,)
	eventName: Optional[str] = Field(alias="eventName", default=None,)
	ipAddress: Optional[str] = Field(alias="ipAddress", default=None,)
	osPlatformDeviceDetails: Optional[str] = Field(alias="osPlatformDeviceDetails", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .click_source import ClickSource
