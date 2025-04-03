from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookChartTitleFormat(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookChartTitleFormat"] = Field(alias="@odata.type", default="#microsoft.graph.workbookChartTitleFormat")
	fill: Optional[WorkbookChartFill] = Field(alias="fill", default=None,)
	font: Optional[WorkbookChartFont] = Field(alias="font", default=None,)

from .workbook_chart_fill import WorkbookChartFill
from .workbook_chart_font import WorkbookChartFont
