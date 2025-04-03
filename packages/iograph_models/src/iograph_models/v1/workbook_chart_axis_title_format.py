from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookChartAxisTitleFormat(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookChartAxisTitleFormat"] = Field(alias="@odata.type", default="#microsoft.graph.workbookChartAxisTitleFormat")
	font: Optional[WorkbookChartFont] = Field(alias="font", default=None,)

from .workbook_chart_font import WorkbookChartFont
