from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookChartTitle(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	overlay: Optional[bool] = Field(default=None,alias="overlay",)
	text: Optional[str] = Field(default=None,alias="text",)
	visible: Optional[bool] = Field(default=None,alias="visible",)
	format: Optional[WorkbookChartTitleFormat] = Field(default=None,alias="format",)

from .workbook_chart_title_format import WorkbookChartTitleFormat

