from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AddWatermark(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	odata_type: Literal["#microsoft.graph.addWatermark"] = Field(alias="@odata.type", default="#microsoft.graph.addWatermark")
	fontColor: Optional[str] = Field(alias="fontColor", default=None,)
	fontSize: Optional[int] = Field(alias="fontSize", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)
	orientation: Optional[PageOrientation | str] = Field(alias="orientation", default=None,)

from .page_orientation import PageOrientation
