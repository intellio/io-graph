from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VerticalSection(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	emphasis: Optional[SectionEmphasisType] = Field(default=None,alias="emphasis",)
	webparts: Optional[list[WebPart]] = Field(default=None,alias="webparts",)

from .section_emphasis_type import SectionEmphasisType
from .web_part import WebPart

