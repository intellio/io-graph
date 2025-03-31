from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAnomalyCorrelationGroupFeature(BaseModel):
	deviceFeatureType: Optional[UserExperienceAnalyticsAnomalyDeviceFeatureType | str] = Field(alias="deviceFeatureType", default=None,)
	values: Optional[list[str]] = Field(alias="values", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .user_experience_analytics_anomaly_device_feature_type import UserExperienceAnalyticsAnomalyDeviceFeatureType
