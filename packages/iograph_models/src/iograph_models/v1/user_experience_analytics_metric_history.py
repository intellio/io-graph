from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsMetricHistory(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deviceId: Optional[str] = Field(alias="deviceId",default=None,)
	metricDateTime: Optional[datetime] = Field(alias="metricDateTime",default=None,)
	metricType: Optional[str] = Field(alias="metricType",default=None,)


