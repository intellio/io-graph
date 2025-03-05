from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookChartPointFormat(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	fill: Optional[WorkbookChartFill] = Field(default=None,alias="fill",)

from .workbook_chart_fill import WorkbookChartFill

