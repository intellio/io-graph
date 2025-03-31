from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_health_metric_time_seriesPostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MetricTimeSeriesDataPoint]] = Field(alias="value", default=None,)

from .metric_time_series_data_point import MetricTimeSeriesDataPoint
