from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookChartLegend(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	overlay: Optional[bool] = Field(alias="overlay",default=None,)
	position: Optional[str] = Field(alias="position",default=None,)
	visible: Optional[bool] = Field(alias="visible",default=None,)
	format: Optional[WorkbookChartLegendFormat] = Field(alias="format",default=None,)

from .workbook_chart_legend_format import WorkbookChartLegendFormat

