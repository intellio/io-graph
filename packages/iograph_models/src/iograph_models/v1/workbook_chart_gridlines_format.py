from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookChartGridlinesFormat(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookChartGridlinesFormat"] = Field(alias="@odata.type", default="#microsoft.graph.workbookChartGridlinesFormat")
	line: Optional[WorkbookChartLineFormat] = Field(alias="line", default=None,)

from .workbook_chart_line_format import WorkbookChartLineFormat
