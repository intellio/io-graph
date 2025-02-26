from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookChartAxisFormat(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	font: Optional[WorkbookChartFont] = Field(default=None,alias="font",)
	line: Optional[WorkbookChartLineFormat] = Field(default=None,alias="line",)

from .workbook_chart_font import WorkbookChartFont
from .workbook_chart_line_format import WorkbookChartLineFormat

