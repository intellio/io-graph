from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAnomalyDevice(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsAnomalyDevice"] = Field(alias="@odata.type",)
	anomalyId: Optional[str] = Field(alias="anomalyId", default=None,)
	anomalyOnDeviceFirstOccurrenceDateTime: Optional[datetime] = Field(alias="anomalyOnDeviceFirstOccurrenceDateTime", default=None,)
	anomalyOnDeviceLatestOccurrenceDateTime: Optional[datetime] = Field(alias="anomalyOnDeviceLatestOccurrenceDateTime", default=None,)
	correlationGroupId: Optional[str] = Field(alias="correlationGroupId", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	deviceManufacturer: Optional[str] = Field(alias="deviceManufacturer", default=None,)
	deviceModel: Optional[str] = Field(alias="deviceModel", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	deviceStatus: Optional[UserExperienceAnalyticsDeviceStatus | str] = Field(alias="deviceStatus", default=None,)
	osName: Optional[str] = Field(alias="osName", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)

from .user_experience_analytics_device_status import UserExperienceAnalyticsDeviceStatus
