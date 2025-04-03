from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookChartSeries(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookChartSeries"] = Field(alias="@odata.type", default="#microsoft.graph.workbookChartSeries")
	name: Optional[str] = Field(alias="name", default=None,)
	format: Optional[WorkbookChartSeriesFormat] = Field(alias="format", default=None,)
	points: Optional[list[WorkbookChartPoint]] = Field(alias="points", default=None,)

from .workbook_chart_series_format import WorkbookChartSeriesFormat
from .workbook_chart_point import WorkbookChartPoint
