from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MetricTimeSeriesDataPoint(BaseModel):
	dateTime: Optional[datetime] = Field(alias="dateTime", default=None,)
	value: Optional[int] = Field(alias="value", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

