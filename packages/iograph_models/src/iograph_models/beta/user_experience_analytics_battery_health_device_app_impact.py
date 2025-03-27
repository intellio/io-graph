from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsBatteryHealthDeviceAppImpact(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	appDisplayName: Optional[str] = Field(alias="appDisplayName", default=None,)
	appName: Optional[str] = Field(alias="appName", default=None,)
	appPublisher: Optional[str] = Field(alias="appPublisher", default=None,)
	batteryUsagePercentage: float | str | ReferenceNumeric
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	isForegroundApp: Optional[bool] = Field(alias="isForegroundApp", default=None,)

from .reference_numeric import ReferenceNumeric

