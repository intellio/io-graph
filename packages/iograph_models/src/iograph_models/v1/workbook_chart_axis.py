from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookChartAxis(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookChartAxis"] = Field(alias="@odata.type", default="#microsoft.graph.workbookChartAxis")
	majorUnit: Optional[str] = Field(alias="majorUnit", default=None,)
	maximum: Optional[str] = Field(alias="maximum", default=None,)
	minimum: Optional[str] = Field(alias="minimum", default=None,)
	minorUnit: Optional[str] = Field(alias="minorUnit", default=None,)
	format: Optional[WorkbookChartAxisFormat] = Field(alias="format", default=None,)
	majorGridlines: Optional[WorkbookChartGridlines] = Field(alias="majorGridlines", default=None,)
	minorGridlines: Optional[WorkbookChartGridlines] = Field(alias="minorGridlines", default=None,)
	title: Optional[WorkbookChartAxisTitle] = Field(alias="title", default=None,)

from .workbook_chart_axis_format import WorkbookChartAxisFormat
from .workbook_chart_gridlines import WorkbookChartGridlines
from .workbook_chart_axis_title import WorkbookChartAxisTitle
