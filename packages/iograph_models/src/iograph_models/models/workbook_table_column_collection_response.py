from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookTableColumnCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[WorkbookTableColumn] = Field(alias="value",)

from .workbook_table_column import WorkbookTableColumn

