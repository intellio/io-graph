from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookChartGridlinesFormat(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	line: Optional[WorkbookChartLineFormat] = Field(alias="line",default=None,)

from .workbook_chart_line_format import WorkbookChartLineFormat

