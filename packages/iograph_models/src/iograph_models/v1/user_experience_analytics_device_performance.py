from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsDevicePerformance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsDevicePerformance"] = Field(alias="@odata.type", default="#microsoft.graph.userExperienceAnalyticsDevicePerformance")
	averageBlueScreens: float | str | ReferenceNumeric
	averageRestarts: float | str | ReferenceNumeric
	blueScreenCount: Optional[int] = Field(alias="blueScreenCount", default=None,)
	bootScore: Optional[int] = Field(alias="bootScore", default=None,)
	coreBootTimeInMs: Optional[int] = Field(alias="coreBootTimeInMs", default=None,)
	coreLoginTimeInMs: Optional[int] = Field(alias="coreLoginTimeInMs", default=None,)
	deviceCount: Optional[int] = Field(alias="deviceCount", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	diskType: Optional[DiskType | str] = Field(alias="diskType", default=None,)
	groupPolicyBootTimeInMs: Optional[int] = Field(alias="groupPolicyBootTimeInMs", default=None,)
	groupPolicyLoginTimeInMs: Optional[int] = Field(alias="groupPolicyLoginTimeInMs", default=None,)
	healthStatus: Optional[UserExperienceAnalyticsHealthState | str] = Field(alias="healthStatus", default=None,)
	loginScore: Optional[int] = Field(alias="loginScore", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	modelStartupPerformanceScore: float | str | ReferenceNumeric
	operatingSystemVersion: Optional[str] = Field(alias="operatingSystemVersion", default=None,)
	responsiveDesktopTimeInMs: Optional[int] = Field(alias="responsiveDesktopTimeInMs", default=None,)
	restartCount: Optional[int] = Field(alias="restartCount", default=None,)
	startupPerformanceScore: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
from .disk_type import DiskType
from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
