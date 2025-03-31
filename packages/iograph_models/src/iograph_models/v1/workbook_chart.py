from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookChart(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookChart"] = Field(alias="@odata.type",)
	height: float | str | ReferenceNumeric
	left: float | str | ReferenceNumeric
	name: Optional[str] = Field(alias="name", default=None,)
	top: float | str | ReferenceNumeric
	width: float | str | ReferenceNumeric
	axes: Optional[WorkbookChartAxes] = Field(alias="axes", default=None,)
	dataLabels: Optional[WorkbookChartDataLabels] = Field(alias="dataLabels", default=None,)
	format: Optional[WorkbookChartAreaFormat] = Field(alias="format", default=None,)
	legend: Optional[WorkbookChartLegend] = Field(alias="legend", default=None,)
	series: Optional[list[WorkbookChartSeries]] = Field(alias="series", default=None,)
	title: Optional[WorkbookChartTitle] = Field(alias="title", default=None,)
	worksheet: Optional[WorkbookWorksheet] = Field(alias="worksheet", default=None,)

from .reference_numeric import ReferenceNumeric
from .workbook_chart_axes import WorkbookChartAxes
from .workbook_chart_data_labels import WorkbookChartDataLabels
from .workbook_chart_area_format import WorkbookChartAreaFormat
from .workbook_chart_legend import WorkbookChartLegend
from .workbook_chart_series import WorkbookChartSeries
from .workbook_chart_title import WorkbookChartTitle
from .workbook_worksheet import WorkbookWorksheet
