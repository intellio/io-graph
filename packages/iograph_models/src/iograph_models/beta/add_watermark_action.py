from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AddWatermarkAction(BaseModel):
	odata_type: Literal["#microsoft.graph.addWatermarkAction"] = Field(alias="@odata.type", default="#microsoft.graph.addWatermarkAction")
	fontColor: Optional[str] = Field(alias="fontColor", default=None,)
	fontName: Optional[str] = Field(alias="fontName", default=None,)
	fontSize: Optional[int] = Field(alias="fontSize", default=None,)
	layout: Optional[WatermarkLayout | str] = Field(alias="layout", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)
	uiElementName: Optional[str] = Field(alias="uiElementName", default=None,)

from .watermark_layout import WatermarkLayout
