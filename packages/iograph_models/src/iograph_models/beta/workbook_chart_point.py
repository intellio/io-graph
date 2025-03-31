from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookChartPoint(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookChartPoint"] = Field(alias="@odata.type",)
	value: Optional[str] = Field(alias="value", default=None,)
	format: Optional[WorkbookChartPointFormat] = Field(alias="format", default=None,)

from .workbook_chart_point_format import WorkbookChartPointFormat
