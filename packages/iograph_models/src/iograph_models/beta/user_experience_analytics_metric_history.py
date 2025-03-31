from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class UserExperienceAnalyticsMetricHistory(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsMetricHistory"] = Field(alias="@odata.type",)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	metricDateTime: Optional[datetime] = Field(alias="metricDateTime", default=None,)
	metricType: Optional[str] = Field(alias="metricType", default=None,)

