from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HorizontalSection(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	emphasis: Optional[SectionEmphasisType] = Field(default=None,alias="emphasis",)
	layout: Optional[HorizontalSectionLayoutType] = Field(default=None,alias="layout",)
	columns: Optional[list[HorizontalSectionColumn]] = Field(default=None,alias="columns",)

from .section_emphasis_type import SectionEmphasisType
from .horizontal_section_layout_type import HorizontalSectionLayoutType
from .horizontal_section_column import HorizontalSectionColumn

