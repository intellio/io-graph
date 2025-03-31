from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WorkbookTableColumnCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WorkbookTableColumn]] = Field(alias="value", default=None,)

from .workbook_table_column import WorkbookTableColumn
