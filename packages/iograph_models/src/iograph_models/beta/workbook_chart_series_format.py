from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookChartSeriesFormat(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookChartSeriesFormat"] = Field(alias="@odata.type",)
	fill: Optional[WorkbookChartFill] = Field(alias="fill", default=None,)
	line: Optional[WorkbookChartLineFormat] = Field(alias="line", default=None,)

from .workbook_chart_fill import WorkbookChartFill
from .workbook_chart_line_format import WorkbookChartLineFormat
