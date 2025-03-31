from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityAddContentFooterAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.addContentFooterAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.addContentFooterAction")
	alignment: Optional[SecurityContentAlignment | str] = Field(alias="alignment", default=None,)
	fontColor: Optional[str] = Field(alias="fontColor", default=None,)
	fontName: Optional[str] = Field(alias="fontName", default=None,)
	fontSize: Optional[int] = Field(alias="fontSize", default=None,)
	margin: Optional[int] = Field(alias="margin", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)
	uiElementName: Optional[str] = Field(alias="uiElementName", default=None,)

from .security_content_alignment import SecurityContentAlignment
