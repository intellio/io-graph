from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WorkbookTableSort(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workbookTableSort"] = Field(alias="@odata.type",)
	fields: Optional[list[WorkbookSortField]] = Field(alias="fields", default=None,)
	matchCase: Optional[bool] = Field(alias="matchCase", default=None,)
	method: Optional[str] = Field(alias="method", default=None,)

from .workbook_sort_field import WorkbookSortField
