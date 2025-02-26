from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookChartAxis(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	majorUnit: Optional[str] = Field(default=None,alias="majorUnit",)
	maximum: Optional[str] = Field(default=None,alias="maximum",)
	minimum: Optional[str] = Field(default=None,alias="minimum",)
	minorUnit: Optional[str] = Field(default=None,alias="minorUnit",)
	format: Optional[WorkbookChartAxisFormat] = Field(default=None,alias="format",)
	majorGridlines: Optional[WorkbookChartGridlines] = Field(default=None,alias="majorGridlines",)
	minorGridlines: Optional[WorkbookChartGridlines] = Field(default=None,alias="minorGridlines",)
	title: Optional[WorkbookChartAxisTitle] = Field(default=None,alias="title",)

from .workbook_chart_axis_format import WorkbookChartAxisFormat
from .workbook_chart_gridlines import WorkbookChartGridlines
from .workbook_chart_gridlines import WorkbookChartGridlines
from .workbook_chart_axis_title import WorkbookChartAxisTitle

