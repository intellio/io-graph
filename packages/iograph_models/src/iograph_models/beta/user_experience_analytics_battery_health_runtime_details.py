from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class UserExperienceAnalyticsBatteryHealthRuntimeDetails(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsBatteryHealthRuntimeDetails"] = Field(alias="@odata.type", default="#microsoft.graph.userExperienceAnalyticsBatteryHealthRuntimeDetails")
	activeDevices: Optional[int] = Field(alias="activeDevices", default=None,)
	batteryRuntimeFair: Optional[int] = Field(alias="batteryRuntimeFair", default=None,)
	batteryRuntimeGood: Optional[int] = Field(alias="batteryRuntimeGood", default=None,)
	batteryRuntimePoor: Optional[int] = Field(alias="batteryRuntimePoor", default=None,)
	lastRefreshedDateTime: Optional[datetime] = Field(alias="lastRefreshedDateTime", default=None,)

