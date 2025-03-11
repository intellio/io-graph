from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AddWatermarkAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	fontColor: Optional[str] = Field(alias="fontColor",default=None,)
	fontName: Optional[str] = Field(alias="fontName",default=None,)
	fontSize: Optional[int] = Field(alias="fontSize",default=None,)
	layout: Optional[WatermarkLayout | str] = Field(alias="layout",default=None,)
	text: Optional[str] = Field(alias="text",default=None,)
	uiElementName: Optional[str] = Field(alias="uiElementName",default=None,)

from .watermark_layout import WatermarkLayout

