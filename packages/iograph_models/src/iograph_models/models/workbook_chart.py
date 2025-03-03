from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookChart(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	height: float | str | ReferenceNumeric
	left: float | str | ReferenceNumeric
	name: Optional[str] = Field(default=None,alias="name",)
	top: float | str | ReferenceNumeric
	width: float | str | ReferenceNumeric
	axes: Optional[WorkbookChartAxes] = Field(default=None,alias="axes",)
	dataLabels: Optional[WorkbookChartDataLabels] = Field(default=None,alias="dataLabels",)
	format: Optional[WorkbookChartAreaFormat] = Field(default=None,alias="format",)
	legend: Optional[WorkbookChartLegend] = Field(default=None,alias="legend",)
	series: Optional[list[WorkbookChartSeries]] = Field(default=None,alias="series",)
	title: Optional[WorkbookChartTitle] = Field(default=None,alias="title",)
	worksheet: Optional[WorkbookWorksheet] = Field(default=None,alias="worksheet",)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .workbook_chart_axes import WorkbookChartAxes
from .workbook_chart_data_labels import WorkbookChartDataLabels
from .workbook_chart_area_format import WorkbookChartAreaFormat
from .workbook_chart_legend import WorkbookChartLegend
from .workbook_chart_series import WorkbookChartSeries
from .workbook_chart_title import WorkbookChartTitle
from .workbook_worksheet import WorkbookWorksheet

