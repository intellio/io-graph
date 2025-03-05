from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookTableColumn(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	index: Optional[int] = Field(default=None,alias="index",)
	name: Optional[str] = Field(default=None,alias="name",)
	values: Optional[str] = Field(default=None,alias="values",)
	filter: Optional[WorkbookFilter] = Field(default=None,alias="filter",)

from .workbook_filter import WorkbookFilter

