from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAddWatermarkAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.addWatermarkAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.addWatermarkAction")
	fontColor: Optional[str] = Field(alias="fontColor", default=None,)
	fontName: Optional[str] = Field(alias="fontName", default=None,)
	fontSize: Optional[int] = Field(alias="fontSize", default=None,)
	layout: Optional[SecurityWatermarkLayout | str] = Field(alias="layout", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)
	uiElementName: Optional[str] = Field(alias="uiElementName", default=None,)

from .security_watermark_layout import SecurityWatermarkLayout

