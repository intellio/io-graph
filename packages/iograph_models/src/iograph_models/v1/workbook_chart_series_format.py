from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookChartSeriesFormat(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	fill: Optional[WorkbookChartFill] = Field(alias="fill", default=None,)
	line: Optional[WorkbookChartLineFormat] = Field(alias="line", default=None,)

from .workbook_chart_fill import WorkbookChartFill
from .workbook_chart_line_format import WorkbookChartLineFormat

