from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class UserExperienceAnalyticsBatteryHealthCapacityDetails(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsBatteryHealthCapacityDetails"] = Field(alias="@odata.type",)
	activeDevices: Optional[int] = Field(alias="activeDevices", default=None,)
	batteryCapacityFair: Optional[int] = Field(alias="batteryCapacityFair", default=None,)
	batteryCapacityGood: Optional[int] = Field(alias="batteryCapacityGood", default=None,)
	batteryCapacityPoor: Optional[int] = Field(alias="batteryCapacityPoor", default=None,)
	lastRefreshedDateTime: Optional[datetime] = Field(alias="lastRefreshedDateTime", default=None,)

