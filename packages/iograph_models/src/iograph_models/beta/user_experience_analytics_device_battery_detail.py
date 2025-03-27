from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsDeviceBatteryDetail(BaseModel):
	batteryId: Optional[str] = Field(alias="batteryId", default=None,)
	fullBatteryDrainCount: Optional[int] = Field(alias="fullBatteryDrainCount", default=None,)
	maxCapacityPercentage: Optional[int] = Field(alias="maxCapacityPercentage", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


