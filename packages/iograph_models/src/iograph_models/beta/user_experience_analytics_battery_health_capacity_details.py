from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsBatteryHealthCapacityDetails(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	activeDevices: Optional[int] = Field(alias="activeDevices",default=None,)
	batteryCapacityFair: Optional[int] = Field(alias="batteryCapacityFair",default=None,)
	batteryCapacityGood: Optional[int] = Field(alias="batteryCapacityGood",default=None,)
	batteryCapacityPoor: Optional[int] = Field(alias="batteryCapacityPoor",default=None,)
	lastRefreshedDateTime: Optional[datetime] = Field(alias="lastRefreshedDateTime",default=None,)


