from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Get_health_metric_time_seriesPostRequest(BaseModel):
	metricName: Optional[str] = Field(alias="metricName", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)


