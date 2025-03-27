from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookChartAxisTitleFormat(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	font: Optional[WorkbookChartFont] = Field(alias="font", default=None,)

from .workbook_chart_font import WorkbookChartFont

