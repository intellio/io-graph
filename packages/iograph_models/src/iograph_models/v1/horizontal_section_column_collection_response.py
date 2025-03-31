from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class HorizontalSectionColumnCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[HorizontalSectionColumn]] = Field(alias="value", default=None,)

from .horizontal_section_column import HorizontalSectionColumn
