from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookRangeViewCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[WorkbookRangeView] = Field(alias="value",)

from .workbook_range_view import WorkbookRangeView

