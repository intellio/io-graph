from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookChartAxes(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookChartAxes"] = Field(alias="@odata.type",)
	categoryAxis: Optional[WorkbookChartAxis] = Field(alias="categoryAxis", default=None,)
	seriesAxis: Optional[WorkbookChartAxis] = Field(alias="seriesAxis", default=None,)
	valueAxis: Optional[WorkbookChartAxis] = Field(alias="valueAxis", default=None,)

from .workbook_chart_axis import WorkbookChartAxis
