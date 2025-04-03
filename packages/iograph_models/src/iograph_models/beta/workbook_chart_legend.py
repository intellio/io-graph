from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookChartLegend(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookChartLegend"] = Field(alias="@odata.type", default="#microsoft.graph.workbookChartLegend")
	overlay: Optional[bool] = Field(alias="overlay", default=None,)
	position: Optional[str] = Field(alias="position", default=None,)
	visible: Optional[bool] = Field(alias="visible", default=None,)
	format: Optional[WorkbookChartLegendFormat] = Field(alias="format", default=None,)

from .workbook_chart_legend_format import WorkbookChartLegendFormat
