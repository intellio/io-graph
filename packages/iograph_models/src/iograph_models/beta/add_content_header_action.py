from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AddContentHeaderAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	alignment: Optional[ContentAlignment | str] = Field(alias="alignment",default=None,)
	fontColor: Optional[str] = Field(alias="fontColor",default=None,)
	fontName: Optional[str] = Field(alias="fontName",default=None,)
	fontSize: Optional[int] = Field(alias="fontSize",default=None,)
	margin: Optional[int] = Field(alias="margin",default=None,)
	text: Optional[str] = Field(alias="text",default=None,)
	uiElementName: Optional[str] = Field(alias="uiElementName",default=None,)

from .content_alignment import ContentAlignment

