from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookChartAxisTitle(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookChartAxisTitle"] = Field(alias="@odata.type", default="#microsoft.graph.workbookChartAxisTitle")
	text: Optional[str] = Field(alias="text", default=None,)
	visible: Optional[bool] = Field(alias="visible", default=None,)
	format: Optional[WorkbookChartAxisTitleFormat] = Field(alias="format", default=None,)

from .workbook_chart_axis_title_format import WorkbookChartAxisTitleFormat
