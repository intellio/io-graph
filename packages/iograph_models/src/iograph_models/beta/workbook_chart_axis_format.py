from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookChartAxisFormat(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookChartAxisFormat"] = Field(alias="@odata.type", default="#microsoft.graph.workbookChartAxisFormat")
	font: Optional[WorkbookChartFont] = Field(alias="font", default=None,)
	line: Optional[WorkbookChartLineFormat] = Field(alias="line", default=None,)

from .workbook_chart_font import WorkbookChartFont
from .workbook_chart_line_format import WorkbookChartLineFormat
