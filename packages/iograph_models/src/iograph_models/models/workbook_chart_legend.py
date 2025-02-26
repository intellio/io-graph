from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookChartLegend(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	overlay: Optional[bool] = Field(default=None,alias="overlay",)
	position: Optional[str] = Field(default=None,alias="position",)
	visible: Optional[bool] = Field(default=None,alias="visible",)
	format: Optional[WorkbookChartLegendFormat] = Field(default=None,alias="format",)

from .workbook_chart_legend_format import WorkbookChartLegendFormat

