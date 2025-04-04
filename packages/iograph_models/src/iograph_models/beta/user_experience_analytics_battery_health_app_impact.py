from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsBatteryHealthAppImpact(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsBatteryHealthAppImpact"] = Field(alias="@odata.type", default="#microsoft.graph.userExperienceAnalyticsBatteryHealthAppImpact")
	activeDevices: Optional[int] = Field(alias="activeDevices", default=None,)
	appDisplayName: Optional[str] = Field(alias="appDisplayName", default=None,)
	appName: Optional[str] = Field(alias="appName", default=None,)
	appPublisher: Optional[str] = Field(alias="appPublisher", default=None,)
	batteryUsagePercentage: float | str | ReferenceNumeric
	isForegroundApp: Optional[bool] = Field(alias="isForegroundApp", default=None,)

from .reference_numeric import ReferenceNumeric
