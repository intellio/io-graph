from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookChartSeries(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	name: Optional[str] = Field(default=None,alias="name",)
	format: Optional[WorkbookChartSeriesFormat] = Field(default=None,alias="format",)
	points: list[WorkbookChartPoint] = Field(alias="points",)

from .workbook_chart_series_format import WorkbookChartSeriesFormat
from .workbook_chart_point import WorkbookChartPoint

