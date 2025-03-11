from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HorizontalSection(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	emphasis: Optional[SectionEmphasisType | str] = Field(alias="emphasis",default=None,)
	layout: Optional[HorizontalSectionLayoutType | str] = Field(alias="layout",default=None,)
	columns: Optional[list[HorizontalSectionColumn]] = Field(alias="columns",default=None,)

from .section_emphasis_type import SectionEmphasisType
from .horizontal_section_layout_type import HorizontalSectionLayoutType
from .horizontal_section_column import HorizontalSectionColumn

