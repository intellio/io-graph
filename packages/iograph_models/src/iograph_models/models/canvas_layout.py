from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CanvasLayout(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	horizontalSections: Optional[list[HorizontalSection]] = Field(default=None,alias="horizontalSections",)
	verticalSection: Optional[VerticalSection] = Field(default=None,alias="verticalSection",)

from .horizontal_section import HorizontalSection
from .vertical_section import VerticalSection

