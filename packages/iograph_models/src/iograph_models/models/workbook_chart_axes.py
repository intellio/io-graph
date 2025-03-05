from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookChartAxes(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	categoryAxis: Optional[WorkbookChartAxis] = Field(default=None,alias="categoryAxis",)
	seriesAxis: Optional[WorkbookChartAxis] = Field(default=None,alias="seriesAxis",)
	valueAxis: Optional[WorkbookChartAxis] = Field(default=None,alias="valueAxis",)

from .workbook_chart_axis import WorkbookChartAxis
from .workbook_chart_axis import WorkbookChartAxis
from .workbook_chart_axis import WorkbookChartAxis

