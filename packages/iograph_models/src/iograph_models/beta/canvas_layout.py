from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CanvasLayout(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	horizontalSections: Optional[list[HorizontalSection]] = Field(alias="horizontalSections",default=None,)
	verticalSection: Optional[VerticalSection] = Field(alias="verticalSection",default=None,)

from .horizontal_section import HorizontalSection
from .vertical_section import VerticalSection

