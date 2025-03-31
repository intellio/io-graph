from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAppHealthApplicationPerformance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsAppHealthApplicationPerformance"] = Field(alias="@odata.type",)
	activeDeviceCount: Optional[int] = Field(alias="activeDeviceCount", default=None,)
	appCrashCount: Optional[int] = Field(alias="appCrashCount", default=None,)
	appDisplayName: Optional[str] = Field(alias="appDisplayName", default=None,)
	appHangCount: Optional[int] = Field(alias="appHangCount", default=None,)
	appHealthScore: float | str | ReferenceNumeric
	appName: Optional[str] = Field(alias="appName", default=None,)
	appPublisher: Optional[str] = Field(alias="appPublisher", default=None,)
	appUsageDuration: Optional[int] = Field(alias="appUsageDuration", default=None,)
	meanTimeToFailureInMinutes: Optional[int] = Field(alias="meanTimeToFailureInMinutes", default=None,)

from .reference_numeric import ReferenceNumeric
