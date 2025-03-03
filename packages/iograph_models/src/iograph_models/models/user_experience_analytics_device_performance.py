from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsDevicePerformance(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	averageBlueScreens: float | str | ReferenceNumeric
	averageRestarts: float | str | ReferenceNumeric
	blueScreenCount: Optional[int] = Field(default=None,alias="blueScreenCount",)
	bootScore: Optional[int] = Field(default=None,alias="bootScore",)
	coreBootTimeInMs: Optional[int] = Field(default=None,alias="coreBootTimeInMs",)
	coreLoginTimeInMs: Optional[int] = Field(default=None,alias="coreLoginTimeInMs",)
	deviceCount: Optional[int] = Field(default=None,alias="deviceCount",)
	deviceName: Optional[str] = Field(default=None,alias="deviceName",)
	diskType: Optional[DiskType] = Field(default=None,alias="diskType",)
	groupPolicyBootTimeInMs: Optional[int] = Field(default=None,alias="groupPolicyBootTimeInMs",)
	groupPolicyLoginTimeInMs: Optional[int] = Field(default=None,alias="groupPolicyLoginTimeInMs",)
	healthStatus: Optional[UserExperienceAnalyticsHealthState] = Field(default=None,alias="healthStatus",)
	loginScore: Optional[int] = Field(default=None,alias="loginScore",)
	manufacturer: Optional[str] = Field(default=None,alias="manufacturer",)
	model: Optional[str] = Field(default=None,alias="model",)
	modelStartupPerformanceScore: float | str | ReferenceNumeric
	operatingSystemVersion: Optional[str] = Field(default=None,alias="operatingSystemVersion",)
	responsiveDesktopTimeInMs: Optional[int] = Field(default=None,alias="responsiveDesktopTimeInMs",)
	restartCount: Optional[int] = Field(default=None,alias="restartCount",)
	startupPerformanceScore: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .disk_type import DiskType
from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

