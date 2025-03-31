from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookTableColumn(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookTableColumn"] = Field(alias="@odata.type",)
	index: Optional[int] = Field(alias="index", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	values: Optional[str] = Field(alias="values", default=None,)
	filter: Optional[WorkbookFilter] = Field(alias="filter", default=None,)

from .workbook_filter import WorkbookFilter
