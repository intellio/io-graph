from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookChartAreaFormat(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	fill: Optional[WorkbookChartFill] = Field(default=None,alias="fill",)
	font: Optional[WorkbookChartFont] = Field(default=None,alias="font",)

from .workbook_chart_fill import WorkbookChartFill
from .workbook_chart_font import WorkbookChartFont

