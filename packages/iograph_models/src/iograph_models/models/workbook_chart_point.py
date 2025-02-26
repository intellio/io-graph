from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookChartPoint(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	value: Optional[str] = Field(default=None,alias="value",)
	format: Optional[WorkbookChartPointFormat] = Field(default=None,alias="format",)

from .workbook_chart_point_format import WorkbookChartPointFormat

