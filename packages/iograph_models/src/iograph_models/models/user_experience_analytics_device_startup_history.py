from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UserExperienceAnalyticsDeviceStartupHistory(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	coreBootTimeInMs: Optional[int] = Field(default=None,alias="coreBootTimeInMs",)
	coreLoginTimeInMs: Optional[int] = Field(default=None,alias="coreLoginTimeInMs",)
	deviceId: Optional[str] = Field(default=None,alias="deviceId",)
	featureUpdateBootTimeInMs: Optional[int] = Field(default=None,alias="featureUpdateBootTimeInMs",)
	groupPolicyBootTimeInMs: Optional[int] = Field(default=None,alias="groupPolicyBootTimeInMs",)
	groupPolicyLoginTimeInMs: Optional[int] = Field(default=None,alias="groupPolicyLoginTimeInMs",)
	isFeatureUpdate: Optional[bool] = Field(default=None,alias="isFeatureUpdate",)
	isFirstLogin: Optional[bool] = Field(default=None,alias="isFirstLogin",)
	operatingSystemVersion: Optional[str] = Field(default=None,alias="operatingSystemVersion",)
	responsiveDesktopTimeInMs: Optional[int] = Field(default=None,alias="responsiveDesktopTimeInMs",)
	restartCategory: Optional[UserExperienceAnalyticsOperatingSystemRestartCategory] = Field(default=None,alias="restartCategory",)
	restartFaultBucket: Optional[str] = Field(default=None,alias="restartFaultBucket",)
	restartStopCode: Optional[str] = Field(default=None,alias="restartStopCode",)
	startTime: Optional[datetime] = Field(default=None,alias="startTime",)
	totalBootTimeInMs: Optional[int] = Field(default=None,alias="totalBootTimeInMs",)
	totalLoginTimeInMs: Optional[int] = Field(default=None,alias="totalLoginTimeInMs",)

from .user_experience_analytics_operating_system_restart_category import UserExperienceAnalyticsOperatingSystemRestartCategory

