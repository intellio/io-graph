from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsMetricHistory(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deviceId: Optional[str] = Field(default=None,alias="deviceId",)
	metricDateTime: Optional[datetime] = Field(default=None,alias="metricDateTime",)
	metricType: Optional[str] = Field(default=None,alias="metricType",)


