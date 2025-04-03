from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsBatteryHealthDeviceRuntimeHistory(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsBatteryHealthDeviceRuntimeHistory"] = Field(alias="@odata.type", default="#microsoft.graph.userExperienceAnalyticsBatteryHealthDeviceRuntimeHistory")
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	estimatedRuntimeInMinutes: Optional[int] = Field(alias="estimatedRuntimeInMinutes", default=None,)
	runtimeDateTime: Optional[str] = Field(alias="runtimeDateTime", default=None,)

