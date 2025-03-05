from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookChartGridlines(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	visible: Optional[bool] = Field(default=None,alias="visible",)
	format: Optional[WorkbookChartGridlinesFormat] = Field(default=None,alias="format",)

from .workbook_chart_gridlines_format import WorkbookChartGridlinesFormat

