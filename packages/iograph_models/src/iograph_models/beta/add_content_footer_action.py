from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AddContentFooterAction(BaseModel):
	odata_type: Literal["#microsoft.graph.addContentFooterAction"] = Field(alias="@odata.type", default="#microsoft.graph.addContentFooterAction")
	alignment: Optional[ContentAlignment | str] = Field(alias="alignment", default=None,)
	fontColor: Optional[str] = Field(alias="fontColor", default=None,)
	fontName: Optional[str] = Field(alias="fontName", default=None,)
	fontSize: Optional[int] = Field(alias="fontSize", default=None,)
	margin: Optional[int] = Field(alias="margin", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)
	uiElementName: Optional[str] = Field(alias="uiElementName", default=None,)

from .content_alignment import ContentAlignment
