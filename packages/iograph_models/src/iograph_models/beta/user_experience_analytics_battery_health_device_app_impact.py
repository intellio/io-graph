from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsBatteryHealthDeviceAppImpact(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsBatteryHealthDeviceAppImpact"] = Field(alias="@odata.type",)
	appDisplayName: Optional[str] = Field(alias="appDisplayName", default=None,)
	appName: Optional[str] = Field(alias="appName", default=None,)
	appPublisher: Optional[str] = Field(alias="appPublisher", default=None,)
	batteryUsagePercentage: float | str | ReferenceNumeric
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	isForegroundApp: Optional[bool] = Field(alias="isForegroundApp", default=None,)

from .reference_numeric import ReferenceNumeric
