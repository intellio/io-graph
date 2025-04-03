from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookChartTitle(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookChartTitle"] = Field(alias="@odata.type", default="#microsoft.graph.workbookChartTitle")
	overlay: Optional[bool] = Field(alias="overlay", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)
	visible: Optional[bool] = Field(alias="visible", default=None,)
	format: Optional[WorkbookChartTitleFormat] = Field(alias="format", default=None,)

from .workbook_chart_title_format import WorkbookChartTitleFormat
