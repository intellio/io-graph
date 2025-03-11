from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookChartAxes(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	categoryAxis: Optional[WorkbookChartAxis] = Field(alias="categoryAxis",default=None,)
	seriesAxis: Optional[WorkbookChartAxis] = Field(alias="seriesAxis",default=None,)
	valueAxis: Optional[WorkbookChartAxis] = Field(alias="valueAxis",default=None,)

from .workbook_chart_axis import WorkbookChartAxis
from .workbook_chart_axis import WorkbookChartAxis
from .workbook_chart_axis import WorkbookChartAxis

