from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class HorizontalSection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.horizontalSection"] = Field(alias="@odata.type", default="#microsoft.graph.horizontalSection")
	emphasis: Optional[SectionEmphasisType | str] = Field(alias="emphasis", default=None,)
	layout: Optional[HorizontalSectionLayoutType | str] = Field(alias="layout", default=None,)
	columns: Optional[list[HorizontalSectionColumn]] = Field(alias="columns", default=None,)

from .section_emphasis_type import SectionEmphasisType
from .horizontal_section_layout_type import HorizontalSectionLayoutType
from .horizontal_section_column import HorizontalSectionColumn
