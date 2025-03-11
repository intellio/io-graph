from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsBatteryHealthRuntimeDetails(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	activeDevices: Optional[int] = Field(alias="activeDevices",default=None,)
	batteryRuntimeFair: Optional[int] = Field(alias="batteryRuntimeFair",default=None,)
	batteryRuntimeGood: Optional[int] = Field(alias="batteryRuntimeGood",default=None,)
	batteryRuntimePoor: Optional[int] = Field(alias="batteryRuntimePoor",default=None,)
	lastRefreshedDateTime: Optional[datetime] = Field(alias="lastRefreshedDateTime",default=None,)


