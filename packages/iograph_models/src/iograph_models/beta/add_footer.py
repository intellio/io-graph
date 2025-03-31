from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AddFooter(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	odata_type: Literal["#microsoft.graph.addFooter"] = Field(alias="@odata.type", default="#microsoft.graph.addFooter")
	fontColor: Optional[str] = Field(alias="fontColor", default=None,)
	fontSize: Optional[int] = Field(alias="fontSize", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)
	alignment: Optional[Alignment | str] = Field(alias="alignment", default=None,)
	margin: Optional[int] = Field(alias="margin", default=None,)

from .alignment import Alignment
