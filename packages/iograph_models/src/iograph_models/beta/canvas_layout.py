from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CanvasLayout(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.canvasLayout"] = Field(alias="@odata.type", default="#microsoft.graph.canvasLayout")
	horizontalSections: Optional[list[HorizontalSection]] = Field(alias="horizontalSections", default=None,)
	verticalSection: Optional[VerticalSection] = Field(alias="verticalSection", default=None,)

from .horizontal_section import HorizontalSection
from .vertical_section import VerticalSection
