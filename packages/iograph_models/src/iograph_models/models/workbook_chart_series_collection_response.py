from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookChartSeriesCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[WorkbookChartSeries] = Field(alias="value",)

from .workbook_chart_series import WorkbookChartSeries

