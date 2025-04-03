from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookChartPointFormat(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookChartPointFormat"] = Field(alias="@odata.type", default="#microsoft.graph.workbookChartPointFormat")
	fill: Optional[WorkbookChartFill] = Field(alias="fill", default=None,)

from .workbook_chart_fill import WorkbookChartFill
