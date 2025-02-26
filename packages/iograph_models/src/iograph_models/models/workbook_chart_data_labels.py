from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookChartDataLabels(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	position: Optional[str] = Field(default=None,alias="position",)
	separator: Optional[str] = Field(default=None,alias="separator",)
	showBubbleSize: Optional[bool] = Field(default=None,alias="showBubbleSize",)
	showCategoryName: Optional[bool] = Field(default=None,alias="showCategoryName",)
	showLegendKey: Optional[bool] = Field(default=None,alias="showLegendKey",)
	showPercentage: Optional[bool] = Field(default=None,alias="showPercentage",)
	showSeriesName: Optional[bool] = Field(default=None,alias="showSeriesName",)
	showValue: Optional[bool] = Field(default=None,alias="showValue",)
	format: Optional[WorkbookChartDataLabelFormat] = Field(default=None,alias="format",)

from .workbook_chart_data_label_format import WorkbookChartDataLabelFormat

