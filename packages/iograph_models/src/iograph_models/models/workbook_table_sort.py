from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkbookTableSort(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	fields: Optional[list[WorkbookSortField]] = Field(alias="fields",default=None,)
	matchCase: Optional[bool] = Field(alias="matchCase",default=None,)
	method: Optional[str] = Field(alias="method",default=None,)

from .workbook_sort_field import WorkbookSortField

