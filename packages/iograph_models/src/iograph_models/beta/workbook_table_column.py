from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookTableColumn(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	index: Optional[int] = Field(alias="index",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	values: Optional[str] = Field(alias="values",default=None,)
	filter: Optional[WorkbookFilter] = Field(alias="filter",default=None,)

from .workbook_filter import WorkbookFilter

