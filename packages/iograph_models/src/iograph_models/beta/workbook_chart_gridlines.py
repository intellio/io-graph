from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookChartGridlines(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	visible: Optional[bool] = Field(alias="visible", default=None,)
	format: Optional[WorkbookChartGridlinesFormat] = Field(alias="format", default=None,)

from .workbook_chart_gridlines_format import WorkbookChartGridlinesFormat

