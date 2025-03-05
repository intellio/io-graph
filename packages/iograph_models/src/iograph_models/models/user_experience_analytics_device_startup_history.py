from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsDeviceStartupHistory(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	coreBootTimeInMs: Optional[int] = Field(alias="coreBootTimeInMs",default=None,)
	coreLoginTimeInMs: Optional[int] = Field(alias="coreLoginTimeInMs",default=None,)
	deviceId: Optional[str] = Field(alias="deviceId",default=None,)
	featureUpdateBootTimeInMs: Optional[int] = Field(alias="featureUpdateBootTimeInMs",default=None,)
	groupPolicyBootTimeInMs: Optional[int] = Field(alias="groupPolicyBootTimeInMs",default=None,)
	groupPolicyLoginTimeInMs: Optional[int] = Field(alias="groupPolicyLoginTimeInMs",default=None,)
	isFeatureUpdate: Optional[bool] = Field(alias="isFeatureUpdate",default=None,)
	isFirstLogin: Optional[bool] = Field(alias="isFirstLogin",default=None,)
	operatingSystemVersion: Optional[str] = Field(alias="operatingSystemVersion",default=None,)
	responsiveDesktopTimeInMs: Optional[int] = Field(alias="responsiveDesktopTimeInMs",default=None,)
	restartCategory: Optional[UserExperienceAnalyticsOperatingSystemRestartCategory | str] = Field(alias="restartCategory",default=None,)
	restartFaultBucket: Optional[str] = Field(alias="restartFaultBucket",default=None,)
	restartStopCode: Optional[str] = Field(alias="restartStopCode",default=None,)
	startTime: Optional[datetime] = Field(alias="startTime",default=None,)
	totalBootTimeInMs: Optional[int] = Field(alias="totalBootTimeInMs",default=None,)
	totalLoginTimeInMs: Optional[int] = Field(alias="totalLoginTimeInMs",default=None,)

from .user_experience_analytics_operating_system_restart_category import UserExperienceAnalyticsOperatingSystemRestartCategory

