from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookChartGridlines(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookChartGridlines"] = Field(alias="@odata.type", default="#microsoft.graph.workbookChartGridlines")
	visible: Optional[bool] = Field(alias="visible", default=None,)
	format: Optional[WorkbookChartGridlinesFormat] = Field(alias="format", default=None,)

from .workbook_chart_gridlines_format import WorkbookChartGridlinesFormat
