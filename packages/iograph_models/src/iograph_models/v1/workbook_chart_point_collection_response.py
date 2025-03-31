from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookChartPointCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WorkbookChartPoint]] = Field(alias="value", default=None,)

from .workbook_chart_point import WorkbookChartPoint
