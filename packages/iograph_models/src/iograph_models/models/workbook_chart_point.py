from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookChartPoint(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	value: Optional[str] = Field(alias="value",default=None,)
	format: Optional[WorkbookChartPointFormat] = Field(alias="format",default=None,)

from .workbook_chart_point_format import WorkbookChartPointFormat

