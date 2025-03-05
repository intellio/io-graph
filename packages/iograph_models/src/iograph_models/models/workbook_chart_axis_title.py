from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookChartAxisTitle(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	text: Optional[str] = Field(default=None,alias="text",)
	visible: Optional[bool] = Field(default=None,alias="visible",)
	format: Optional[WorkbookChartAxisTitleFormat] = Field(default=None,alias="format",)

from .workbook_chart_axis_title_format import WorkbookChartAxisTitleFormat

