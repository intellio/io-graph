from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookChartPointCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[WorkbookChartPoint]] = Field(default=None,alias="value",)

from .workbook_chart_point import WorkbookChartPoint

