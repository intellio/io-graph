from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookChartDataLabels(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	position: Optional[str] = Field(alias="position",default=None,)
	separator: Optional[str] = Field(alias="separator",default=None,)
	showBubbleSize: Optional[bool] = Field(alias="showBubbleSize",default=None,)
	showCategoryName: Optional[bool] = Field(alias="showCategoryName",default=None,)
	showLegendKey: Optional[bool] = Field(alias="showLegendKey",default=None,)
	showPercentage: Optional[bool] = Field(alias="showPercentage",default=None,)
	showSeriesName: Optional[bool] = Field(alias="showSeriesName",default=None,)
	showValue: Optional[bool] = Field(alias="showValue",default=None,)
	format: Optional[WorkbookChartDataLabelFormat] = Field(alias="format",default=None,)

from .workbook_chart_data_label_format import WorkbookChartDataLabelFormat

